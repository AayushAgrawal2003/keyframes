import numpy as np
import cv2 as cv 
 



# itr through the frames
# Read the video 


cap = cv.VideoCapture('main.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Frame',frame)
        # Add the frame extraction code here 

        # Calculate the laplac value and compare it to a threshold 
        