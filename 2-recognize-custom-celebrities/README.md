# Recognize Custom Celebrities
In this module you will learn how to use Amazon Rekognition to recognize other public figures that Rekognition celebrity API does does not detect today. You will index faces of custom celebrities and then analyze few images and video to recognize those celebrities.

1. Open SageMaker instance you created in previous module.

2. From home screen, click on folder celebrity-recognition and then 2-recognize-custom-celebrities.

![](assets/sagemaker-notebook-folder.png)

3. Click on the Jupyter notebook CustomCelebrityRecognition and follow instructions in the notebook.

![](assets/notebook-home.png)

4. You will see custom celebrities recognized in the image and video as below.

![](assets/custom-image.png)

![](assets/custom-video.png)

## Completion
You have successfully created Rekognition collection, indexed faces and recognized public figures in images and videos. In the next module, [Who's Who App](../3-whos-who-app), you will learn how to combine both RecognizeCelebrity and SearchFaceByImage to build a web app which can recognize public figures.
