# Build a "Who's Who" App for Your Media Content

Video has become an increasingly successful medium for advertising, marketing, and engaging customers. However, many companies underutilize their substantial video assets because they are poorly indexed and cataloged. In this workshop, learn how to use machine learning services to gain more value from video by building a customer celebrity detection feature that can recognize mainstream celebrities and individuals from your own uploaded media files.

In this workshop, we will use following AWS services:

* Amazon Rekognition
* Amazon DynamoDB
* AWS Lambda
* Amazon API Gateway
* Amazon S3

## Learning Objectives

* Learn how to recognize celebrities in images and video using Amazon Rekognition.
* Learn how to create and manage Rekognition collections and index faces of custom celebrities to get recognized.
* Learn how to build an end to end solution like Prime Video X-Ray to recognize mainstream and custom celebrities.

## Pre-requisites

### AWS Account

In order to complete this workshop you will need an AWS Account with access to AWS IAM, Amazon S3, Amazon DynamoDB, AWS Lambda, AWS Step Functions, Amazon API Gateway and Amazon Rekognition.

All of the resources you will launch as part of this workshop are eligible for the AWS free tier if your account is less than 12 months old. See the [AWS Free Tier page](https://aws.amazon.com/free/) for more details.

## Modules

This workshop has following three modules.

1. [Celebrity Recognition](1-celebrity-recognition)
2. [Recognize Custom Celebrities](2-recognize-custom-celebrities)
3. [Who's Who App](3-whos-who-app)

## Cleanup
After you have completed the workshop, you can delete all of the resources using the following steps:
1. Delete all Lambda functions created manually
2. Delete all CloudFormation stacks created in the first module
