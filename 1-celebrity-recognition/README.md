# Celebrity Recognition

In this module you will learn about Celebrity API of Amazon Rekognition which can recognize thousands of celebrities in a wide range of categories, such as entertainment and media, sports, business, and politics. With Amazon Rekognition, you can recognize celebrities in images and in stored videos. You can also get additional information for recognized celebrities.

## Create and Instance to run Jupyter

In this step we will create a SageMaker Notebook instance using CloudFormation template.


In this step we will create a SageMaker Notebook instance using CloudFormation template so we can use Jupyter Notebook to prototype.

***SageMaker or Jupyter Notebook is not required to use Rekognition, but we will use Jupyter as IDE for quick prototyping and to learn various Rekognition APIs.***

1. Click on one of the buttons below to launch CloudFormation template in an AWS region.

Region| Launch
------|-----
US East (N. Virginia) | [![Create SageMaker Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=celebrity-recognition&templateURL=https://s3.amazonaws.com/aws-workshops-us-east-1/celebrity-rekognition/deployment/cf-sage-maker.yaml)
US East (Ohio) | [![Create SageMaker Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?stackName=celebrity-recognition&templateURL=https://s3.us-east-2.amazonaws.com/aws-workshops-us-east-2/celebrity-rekognition/deployment/cf-sage-maker.yaml)
US West (Oregon) | [![Create SageMaker Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=celebrity-recognition&templateURL=https://s3-us-west-2.amazonaws.com/aws-workshops-us-west-2/celebrity-rekognition/deployment/cf-sage-maker.yaml)
EU (Ireland) | [![Create SageMaker Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/create/review?stackName=celebrity-recognition&templateURL=https://s3-eu-west-1.amazonaws.com/aws-workshops-eu-west-1/celebrity-rekognition/deployment/cf-sage-maker.yaml)


2. Under Create stack, check the checkbox for "I acknowledge that AWS CloudFormation might create IAM resources with custom names" and click Create.

![](assets/cf-1.png)


3. You should now see the screen with status CREATE_IN_PROGRESS. Click on the Stacks link in the top navigation and then click Refresh icon to see current CloudFormation stacks.

![](assets/cf-2.png)


4. Click on the checkbox next to the stack to see additional details below and wait until CloudFormation stack has the status CREATE_COMPLETE.

![](assets/cf-3.png)


## Open SageMaker Instance

1. After CloudFormation template is complete, Click on the Output tab and click on the link for NotebookInstanceName.

![](assets/cf-4.png)

2. From your SageMaker instance click on the Open button.

![](assets/cf-5.png)

3. You will now be redirected to the Jupyter UI.

![](assets/jupyter-home.png)

4. Click on New and then Terminal.

![](assets/sagemaker-new-terminal.png)

5. You should now see Terminal like below:

![](assets/sagemaker-terminal.png)

6. In the terminal type:
- cd SageMaker
- git clone https://github.com/darwaishx/celebrity-recognition.git

![](assets/sagemaker-gitclone.png)

7. Go back to Jupyter home screen by clicking on the Jupyter logo on the top left and refresh to see the folder celebrity-recognition.

![](assets/git-folder.png)

8. Click on celebrity-recognition, then 1-celebrity-recognition and then CelebrityRecognition.ipynb to open the notebook.

![](assets/m1-notebook.png)

9. Follow the directions in the notebook to run each cell and review it's output. You will see celebrities identified in image and video as below.

![](assets/m1-celeb.png)

![](assets/m1-celeb-video.png)

## Completion
You have successfully used Amazon Rekognition to identify celebrities in images an videos. In the next module, [Recognize Custom Celebrities ](../2-recognize-custom-celebrities), you will learn how to recognize your custom celebrities in the images and videos.
