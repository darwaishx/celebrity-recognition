import json
import boto3
import time
from collections import OrderedDict

def getDynamoDBItem(itemId, dynamodb, ddbTableName):
    ddbGetItemResponse = dynamodb.get_item(
        Key={'id': {'S': itemId} },
        TableName=ddbTableName
    )

    itemToReturn = ('', '', '')

    if('Item' in ddbGetItemResponse):
        itemToReturn = (ddbGetItemResponse['Item']['id']['S'],
                ddbGetItemResponse['Item']['name']['S'],
                ddbGetItemResponse['Item']['url']['S'])

    return itemToReturn

def getCelebrities(rekognition, celebrityJobId):
    getCelebrityRecognition = rekognition.get_celebrity_recognition(
    JobId=celebrityJobId,
        SortBy='TIMESTAMP')

    while(getCelebrityRecognition['JobStatus'] == 'IN_PROGRESS'):
        time.sleep(5)
        print('.', end='')

        getCelebrityRecognition = rekognition.get_celebrity_recognition(
        JobId=celebrityJobId,
        SortBy='TIMESTAMP')

    print(getCelebrityRecognition['JobStatus'])

    return getCelebrityRecognition

def getFaces(rekognition, faceSearchJobId):
    getFaceSearch = rekognition.get_face_search(
        JobId=faceSearchJobId,
        SortBy='TIMESTAMP'
    )

    while(getFaceSearch['JobStatus'] == 'IN_PROGRESS'):
        time.sleep(5)
        print('.', end='')

        getFaceSearch = rekognition.get_face_search(
        JobId=faceSearchJobId,
        SortBy='TIMESTAMP')

    print(getFaceSearch['JobStatus'])

    return getFaceSearch

def mergeResults(rekognition, dynamodb, ddbTableName, cjid, fjid):
    c = getCelebrities(rekognition, cjid)
    f = getFaces(rekognition, fjid)

    recognizedCelebrities = {}
    celebsData = {}

    for rc in c['Celebrities']:
        rc_cl = float(rc['Celebrity']['Confidence'])
        if(rc_cl > 80):
            if(rc['Timestamp'] in recognizedCelebrities):
                recognizedCelebrities[rc['Timestamp']].append(rc)
            else:
                recognizedCelebrities[rc['Timestamp']] = [rc]

    for rp in f['Persons']:
        if('Face' in rp['Person']):
            rp_ts = rp['Timestamp']
            rp_bb = rp['Person']['Face']['BoundingBox']
            if('FaceMatches' in rp and len(rp['FaceMatches']) > 0):
                rp_faceMatch = rp['FaceMatches'][0]
                rp_faceMatch_Similarity = float(rp_faceMatch['Similarity'])
                rp_faceMatch_ExternalImageId = rp_faceMatch['Face']['ExternalImageId']

                if(rp_faceMatch_ExternalImageId in celebsData):
                    cdata = celebsData[rp_faceMatch_ExternalImageId]
                else:
                    cdata = getDynamoDBItem(rp_faceMatch_ExternalImageId, dynamodb, ddbTableName)
                    celebsData[rp_faceMatch_ExternalImageId] = cdata


                rf = {'Timestamp' : rp_ts, 'Id' : rp_faceMatch_ExternalImageId, 'Name' : cdata[1], 'Url' : cdata[2],
                      'Confidence' : rp_faceMatch_Similarity, 'BoundingBox' : rp_bb}

                if(rp_ts in recognizedCelebrities):
                    recognizedCelebrities[rp_ts].append(rf)
                else:
                    recognizedCelebrities[rp_ts] = [rf]

    finalList = []

    od = OrderedDict(sorted(recognizedCelebrities.items()))
    for key, value in od.items():
        for ec in value:
            finalList.append(ec)
    return {'Celebrities': finalList}


def lambda_handler(event, context):

    collectionId = "my-celebrities"
    ddbTableName = "my-celebrities"

    bucketName = event['Records'][0]['s3']['bucket']['name']
    fileName = event['Records'][0]['s3']['object']['key']

    if(not fileName.lower().endswith("mp4")):
        return

    rekognition = boto3.client('rekognition')
    dynamodb = boto3.client('dynamodb')

    celebsResponse = rekognition.start_celebrity_recognition(
        Video={
            'S3Object': {
                'Bucket': bucketName,
                'Name': fileName,
            }
        }
    )

    facesResponse = rekognition.start_face_search(
        Video={
            'S3Object': {
                'Bucket': bucketName,
                'Name': fileName,
            }
        },
        ClientRequestToken='vj',
        FaceMatchThreshold=80,
        CollectionId=collectionId,
    )

    results = mergeResults(rekognition, dynamodb, ddbTableName, celebsResponse['JobId'], facesResponse['JobId'])
    jd = json.dumps(results)

    s3 = boto3.resource('s3')
    obj = s3.Object(bucketName,fileName + "-results.json")
    obj.put(Body=jd)

    return {
        "statusCode": 200,
        "body": jd
    }
