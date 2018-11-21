# 4501Project：Image Style Transfer and Gui Building
## Group Members: Tao Li, Jiaxing Wan, Jiali Sun, Xiaojian Fan
## Main Objective
The main objective of this project is to enable users to transfer the style of their images, either an uploaded image or an image captured by their computer built-in camera when they click on the button `upload via camera` into any style they prefer, for example, it can provide the users with the magic capacity to paint like Vincent van Gogh!<br> 
<br>
A GUI is built to make it more easily to be operated by the users, especially the layman without the necessity to understand the code. Additionally, the working process and the final result can be more observable.<br>
<br>
## Convolutional Neural Network (CNN)
CNN is a technique introduced by Gatys et al. (2015) in their paper 'Image Style Transfer Using Convolutional Neural Network'. The algotithm allows us to separate and recombine the image content and style of natural images. In another words, it is capable of extracting content information from a image and then extract style information from a famous artwork, then combine them together to produce a new image that possesses the content of the photo and the appearance of a given artwork. The key idea backed up this algorithm is to optimise an image with the objective of matching desired CNN feature distributions, which involves both the photo's content information and the artwork's style information.<br>
<br>
You can now go to the **Example** section to firstly have a basic idea before reading the specific **code** part.<br>
<br>
## GUI
The main interface is shown as below:<br>
插入主界面图片！！<br>
<br>
As can be seen, there are three buttons on the main interface: <br>
<br>
`Upload Art`, when this button is clicked, it allows user to select an image (could be the famous artwork or any other images that the user want to extract the image's style) from their own computer, which if satisfies the format requirement, will be displayed on the left-hand-side of the interface. One important thing to be notified here is that only the 'jpg','jpeg','png','bmp' type of file can be uploaded, if the user try to upload one file other than these specified four or no file is selected, there will be a error message box popuped with the massage shown as "Please try to upload a 'jpg','jpeg','png','bmp' file.". <br>
<br>
`Upload your picture`, the button in the middle, when this one is clicked, there will be a pop-up window with two other buttons indicating the two ways that the user can choose between to upload one picture that the user want to extract content information from: `Upload via local`: choose one from users' computer, `Upload via camera`: open computer's camera to take a photo. After one picture is seccessfully uploaded, it will be shown in the right-hand-side of the interface.<br>
<br>
After two pictures both have been uploaded, the user can finally click `process` button, a window will be pop-upped, showing the users with ten intermediate points in the convolutional process and finally end up with the final result displayed on the screen. In this way, the in addition to the final result, users can also see the convolutional process, which make it more transparent and interesting. <br>
<br>
## Code Explaination
<br>
## Examples
<br>
## Requirements
<br>








  
## References
L. A. Gatys, A. S. Ecker, and M. Bethge, “A neural algorithm of artistic style,” ArXiv e-prints, Aug. 2015.
