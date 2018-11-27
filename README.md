# 4501Project：Paint Style Transformation
## Section1, Group Name: PythonGroup, Group Members: Tao Li, Jiaxing Wan, Jiali Sun, Xiaojian Fan
## Main Objective
The main objective of this project is to enable users to transfer the style of their images, either an uploaded image or an image captured by their computer built-in camera when they click on the button `upload via camera` into any style they prefer, for example, it can provide the users with the magic capacity to paint like Vincent van Gogh!<br> 
<br>
A GUI is built to make it more easily to be operated by the users, especially the layman without the necessity to understand the code. Additionally, the working process and the final result can be more observable.<br>
<br>
## Convolutional Neural Network (CNN)
CNN is a technique introduced by Gatys et al. (2015) in their paper 'Image Style Transfer Using Convolutional Neural Network' (http://openaccess.thecvf.com/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf). The algotithm allows us to separate and recombine the image content and style of natural images. In another words, it is capable of extracting content information from a image and then extract style information from a famous artwork, then combine them together to produce a new image that possesses the content of the photo and the appearance of a given artwork. The key idea backed up this algorithm is to optimise an image with the objective of matching desired CNN feature distributions, which involves both the photo's content information and the artwork's style information.<br>
<br>

## GUI
The main interface is shown as below:<br>
插入主界面图片！！<br>
<br>
As can be seen, there are three buttons on the main interface: <br>
<br>
`Upload Art`, when this button is clicked, it allows user to select an image (could be the famous artwork or any other images that the user want to extract the image's style) from their own computer, which if satisfies the format requirement, will be displayed on the left-hand-side of the interface. One important thing to be notified here is that only the 'jpg','jpeg','png','bmp' type of file can be uploaded, if the user try to upload one file other than these specified four or no file is selected, there will be a error message box popup with the massage shown as "Please try to upload a 'jpg','jpeg','png','bmp' file.". <br>
<br>
`Upload your picture`, the button in the middle, when this one is clicked, there will be a pop-up window with two other buttons indicating the two ways that the user can choose between to upload one picture that the user want to extract content information from: `Upload via local`: choose one from users' computer, `Upload via camera`: open computer's camera to take a photo. After one picture is seccessfully uploaded, it will be shown in the middle of the interface.<br>
<br>
After two pictures both have been uploaded, the user can finally click `process` button, a window will pop-up, showing the users with ten intermediate points in the convolutional process and finally end up with the final result displayed on the right-hand side of the main interface. The window showing the convolutional process will be closed automatically. In this way, in addition to the final result, users can also see the convolutional process, which make it more transparent and interesting. <br>
## Requirements
Download opencv, using code `pip install cv2`<br>
Download tensorflow, using code `pip install tensorflow`, server for CNN work<br>
<br>
Pyhton packages to be imported:<br>
import tkinter as tk <br>
from tkinter import filedialog <br>
from PIL import Image, ImageTk <br>
import tkinter.messagebox <br>
import cv2 <br>
import os <br>
import numpy as np <br>
import scipy.misc <br>
import scipy.io <br>
import math <br>
import tensorflow as tf <br>
from sys import stderr <br>
from functools import reduce <br>
import time <br>
<br>
## Run Instructions
Use bash `cd` command, go to the directory in which you want to save the file. Then, use the bash command, `git pull origin master` to download the file. Following this, use the code `python` plus the project name to run the project, the main gui will appear. 
<br>









  
## References
L. A. Gatys, A. S. Ecker, and M. Bethge, “A neural algorithm of artistic style,” ArXiv e-prints, Aug. 2015.
