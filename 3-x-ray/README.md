# X-Ray
In this module we will build an end to end solution like Prime Video X-Ray to recognize mainstream and custom celebrities. We use RecognizeCelebrities and SearchFacesByImage APIs to recognize mainstream and custom celebrities.

## Pre-requisites
This module requires completion of previous modules:
 - [Celebrity Recognition](https://github.com/darwaishx/celebrity-recognition/tree/master/1-celebrity-recognition)
 - [Recognize Custom Celebrities](https://github.com/darwaishx/celebrity-recognition/tree/master/2-recognize-custom-celebrities)

## Deploy Solution

![](assets/X-ray_Lab.png)

In this section we will deploy the solution using CloudFormation template. This CloudFormation template will create required resources for this solution including Lambda functions, API Gateway endpoint and a HTML based client to test the solution.

1. Click on **Launch Stack** button below to launch CloudFormation template in US East AWS region.

Region| Launch
------|-----
US East (N. Virginia) | [![Create IAM Role for SageMaker us-east-1](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=X-Ray&templateURL=https://s3.amazonaws.com/husbasit-dl-artifacts/AnalyzeImage.yaml)

2. Under Create stack, check both checkboxes for **I acknowledge that AWS CloudFormation might create IAM resources with custom names** and **I acknowledge that AWS CloudFormation might create IAM resources.**. Click **Create Change Set** button.

![](assets/Cf1.png)

3. Click on **Execute** button.

![](assets/Cf2.png)

4. You should now see the screen with status **CREATE_IN_PROGRESS**. Click on the **Stacks** link in the top navigation to see current CloudFormation stacks.

![](assets/Cf3.png)

5. Click on the checkbox next to the stack to see additional details below.

![](assets/Cf4.png)

6. Wait until CloudFormation stack status changes to  **CREATE_COMPLETE**.

![](assets/Cf5.png)

7. Click on **Outputs** tab to view the details of Lambda function, API Gateway APIs and Client HTML file created by CloudFormation.

![](assets/Cf6.png)

8. Copy and paste these variable in a text editor of your choice on your local machine for reference. We will use the value of these variables in next steps and sections.

9. Click the **bucketURL** link to load the client HTML page hosted from your S3 bucket.

![](assets/Cf7.png)

10. Following is the UX for Client HTML. You will notice that when you click on **Recognize Celebrities** button, an error is displayed **Error: Invalid API endpoint. Please configure the correct endpoint.**.

![](assets/ClientHtml1.png)

## Verify Lambda environment variables
In this section we need to verify that environment variables defined in Lambda function are set to correct values i.e. pointing to right DynamoDB table and custom Rekognition collection created in previous lab.

1. Go to AWS Lambda in AWS Console at https://console.aws.amazon.com/lambda/

2. Enter your CloudFormation Stack name in the Search text box and press **Enter** key. This will show a list of functions. Click on the function name ending in **-RecognizeCelebrities**

![](assets/Lambda1.png)

3. Scroll down to see **Environment variables** section. Verify if the environment variables **dynamodbTable** and **rekCollectionName** point to correct values. **dynamodbTable** should point to the DynamoDB Table you created in your previous lab to store custom celebrity data. **rekCollectionName** should point to the custom Rekognition Collection you created in the previous lab.

![](assets/Lambda2.png)

## Modify HTML Client
In this section we will modify the HTML Client to point it to the REST endpoint service we have deployed on API Gateway using CloudFormation.

1. Copy the value of **S3Bucket** variable from the reference variables you copied to text editor in **Step 8** of previous section **OR** Repeat **Step 7** of previous section and copy the value for **S3Bucket** from **Outputs**.

2. Go to Amazon S3 in AWS Console at https://s3.console.aws.amazon.com/s3/

3. Type the name of S3 bucket copied in **Step 1** in **Search for buckets** textbox. It will display the bucket in the list. Click on the Bucket name as shown in this screen shot.

![](assets/ClientHtml2.png)

4. Contents of this S3 bucket will have **xray.html** file. Click on **xray.html** file.

![](assets/ClientHtml3.png)

5. Click on **Download** button and save **xray.html** to your local machine.

![](assets/ClientHtml4.png)

6. Open **xray.html** on your local machine using a text editor of your choice. Search for the following line in **xray.html** code. We need to update **apiGatewayUrl** variable to correct URL.
```
apiGatewayUrl = 'TODO: Enter the path to your API Gateway endpoint'
```
7. We need to get the REST endpoint from API Gateway. Go to Amazon API Gateway in AWS Console at https://console.aws.amazon.com/apigateway/.

8. API will be named the same as your CloudFormation stack name. Click on the API in the left menu under **API** section.

![](assets/apigw1.png)

9. As shown in following screen shot, click on **Stages** in left menu under your **API** name. Then click **Prod** -> **POST** under **Stages** as shown in screen shot. Copy the value of **Invoke URL**. This is the endpoint your Client HTML should point to.

![](assets/apigw2.png)

10. Go to the text editor on your local machine where **xray.html** was being edited in **Step 6**. Replace the text **TODO: Enter the path to your API Gateway endpoint** with the recently copied API Gateway endpoint from **Step 9**.
```
apiGatewayUrl = 'https://th123abcd1.execute-api.us-east-1.amazonaws.com/Prod/RecognizeCelebrities'
```
11. Save the file **xray.html**.

## Upload xray.html to S3 bucket

1. Go to Amazon S3 in AWS Console at https://s3.console.aws.amazon.com/s3/

2. Type the name of S3 bucket copied in **Step 1** in **Search for buckets** textbox. It will display the bucket in the list. Click on the Bucket name as shown in this screen shot.

![](assets/ClientHtml2.png)

3. Click on **Upload** button.

![](assets/S3upload1.png)

4. Click on **Add Files** button and select **xray.html** in the file selection dialog from your local machine **OR** drag and drop **xray.html** file on the **Upload** dialog box.

![](assets/S3upload3.png)

5. Click on **Next** button to proceed to **Set permissions**. Select **Grant public read access to this object(s)** from **Manage public permissions** drop-down menu. Click **Next** button.

![](assets/S3upload4.png)

6. Click **Next** button on **Set properties** screen.

7. Review and click **Upload** on **Review** screen.

## Test the solution

1. Access your hosted client HTML page again.

 **Hint:** if you don't have the URL, you can get it from CloudFormation Stack **bucketURL** Output variable  **OR** Repeat **Step 7** of [Deploy Solution](#deploy-solution) and copy the value for **bucketURL** from **Outputs**.

2. Click on **Recognize Celebrities** button and you will see the output(response) coming from Amazon Rekognition.


## Completion
You have successfully created Amazon Prime X-Ray feature using AWS Rekognition, AWS Lambda, API Gateway. This solution recognizes mainstream celebrities as well as custom celebrities.

## Clean up
TODO: Basit to modify Cloudformation template.
