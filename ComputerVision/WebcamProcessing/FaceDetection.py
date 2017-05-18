#Simple Example to display webcam images on the screen
#Adapted from http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
#Author: Brian Mcdonald
#import numpy and opencv
import numpy as np
import cv2

CASCADE_PATH="cascade"
CLASSIFIER_FILE="haarcascade_frontalface_default.xml"

#main method
def main():
    #Open up capture of Video Device - 0 will be 1st webcam, 1 will be 2nd
    cap = cv2.VideoCapture(0)
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(CASCADE_PATH+"\\"+CLASSIFIER_FILE)
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
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(gray,scaleFactor=2,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE)
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #show the image in a window
        cv2.imshow('frame',frame)

    #release the camera
    cap.release()
    #destroy the window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
