#Simple Example to display images onto the screen using OpenCV
#Adapted from http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
#Author: Brian Mcdonald
#import numpy and opencv
import numpy as np
import cv2

#folder for images
IMAGE_FOLDER="media"
#our test image
TEST_IMAGE_NAME="testimage.jpg"

#main method
def main():
    #load in an image as colour
    img = cv2.imread(IMAGE_FOLDER+"\\"+TEST_IMAGE_NAME,cv2.IMREAD_COLOR)
    #show image in a window
    cv2.imshow('image',img)
    #wait for any key to be pressed
    cv2.waitKey(0)
    #destroy window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
