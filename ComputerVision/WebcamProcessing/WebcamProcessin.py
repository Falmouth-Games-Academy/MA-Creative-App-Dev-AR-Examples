#Simple Example to display webcam images on the screen
#Adapted from http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
#Author: Brian Mcdonald
#import numpy and opencv
import numpy as np
import cv2

NORMAL_DISPLAY=1
GRAY_DISPLAY=2
BLUR_DISPLAY=3
SOBEL_DISPLAY=4

#main method
def main():
    DISPLAY_MODE=NORMAL_DISPLAY
    #Open up capture of Video Device - 0 will be 1st webcam, 1 will be 2nd
    cap = cv2.VideoCapture(0)
    #variable for key press
    key=''
    #loop until escape key has been pressed (27)
    while(key!=27):
        #get a key press
        key=cv2.waitKey(1)
        #Capture from webcam, ret is the demensions and frame is the actual image
        ret, frame = cap.read()
        
        # converting to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imageToProcess = cv2.GaussianBlur(gray,(3,3),0)
        sobelx = cv2.Sobel(imageToProcess,cv2.CV_64F,1,0,ksize=5)
        #check for keys 1 - 6 and change image
        if (chr(key & 255)=='1'):
            DISPLAY_MODE=NORMAL_DISPLAY
        elif (chr(key & 255)=='2'):
            DISPLAY_MODE=GRAY_DISPLAY
        elif (chr(key & 255)=='3'):
            DISPLAY_MODE=BLUR_DISPLAY
        elif (chr(key & 255)=='4'):
            DISPLAY_MODE=SOBEL_DISPLAY
        #laplacian = cv2.Laplacian(imageToProcess,cv2.CV_64F)
        #show the image in a window
        if (DISPLAY_MODE==NORMAL_DISPLAY):
            cv2.imshow('frame',frame)
        elif(DISPLAY_MODE==GRAY_DISPLAY):
            cv2.imshow('frame',gray)
        elif(DISPLAY_MODE==BLUR_DISPLAY):
            cv2.imshow('frame',imageToProcess)
        elif(DISPLAY_MODE==SOBEL_DISPLAY):
            cv2.imshow('frame',sobelx)

    #release the camera
    cap.release()
    #destroy the window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
