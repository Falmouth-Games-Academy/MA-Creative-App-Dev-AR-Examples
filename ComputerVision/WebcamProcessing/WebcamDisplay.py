#Simple Example to display webcam images on the screen
#Adapted from http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
#Author: Brian Mcdonald
#import numpy and opencv
import numpy as np
import cv2

#main method
def main():
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
        #show the image in a window
        cv2.imshow('frame',frame)

    #release the camera
    cap.release()
    #destroy the window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
