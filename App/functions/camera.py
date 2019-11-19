import numpy as np
import cv2
from functions.faceapi import detect


def cameraCapture(auth_client, video_capture=0):
    """
    Camera Stream with Open CV 2 on Laptop
    """

    cap = cv2.VideoCapture(video_capture)
    #set the width and height, and UNSUCCESSFULLY set the exposure time

    cap.set(3,1080)
    cap.set(4,1024)
    cap.set(15, 0.1)
    
    while (cap.isOpened()):
        
        video_frame_captured, video_frame = cap.read()

        gray_video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
        gray_video_frame = cv2.equalizeHist(gray_video_frame)

        #Detect the input
        if(video_frame_captured is True):
            
            d = detect(auth_client, video_frame)
            print(d)

        #Show the box
        cv2.imshow("input",video_frame)
        
        key = cv2.waitKey(10)

        if key == 27:
            break

    cv2.destroyAllWindows() 
    cv2.VideoCapture(0).release()
