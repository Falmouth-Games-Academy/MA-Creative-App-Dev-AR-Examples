#Simple Example showing edge detection
#Adapted from
#http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php
#Author: Brian McDonald

#import numpy, opencv
import numpy as np
import cv2

#folder for images
IMAGE_FOLDER="media"
#our test image
TEST_IMAGE_NAME="testimage.jpg"

WINDOW_NAME="Image Processing"


#main method
def main():
    #load in an image as colour
    img = cv2.imread(IMAGE_FOLDER+"\\"+TEST_IMAGE_NAME,cv2.IMREAD_COLOR)
    #convert to greyscale, most edge detction filters use greyscale images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #filter out noise
    imageToProcess = cv2.GaussianBlur(gray,(3,3),0)
    #edge detection filter
    laplacian = cv2.Laplacian(imageToProcess,cv2.CV_64F)
    sobelx = cv2.Sobel(imageToProcess,cv2.CV_64F,1,0,ksize=5)  # x
    sobely = cv2.Sobel(imageToProcess,cv2.CV_64F,0,1,ksize=5)  # y

    #setup a variable to track the current image
    currentImage=img

    #show a window
    cv2.namedWindow(WINDOW_NAME)
    #display the orginal image
    cv2.imshow(WINDOW_NAME,currentImage)
    #wait for any key to be pressed
    key=''
    #loop until escape key(27) is pressed
    while(key!=27):
        #get a key
        key=cv2.waitKey(30)
        #check for keys 1 - 6 and change image
        if (chr(key & 255)=='1'):
            currentImage=img;
        elif (chr(key & 255)=='2'):
            currentImage=gray
        elif (chr(key & 255)=='3'):
            currentImage=imageToProcess
        elif (chr(key & 255)=='4'):
            currentImage=laplacian
        elif (chr(key & 255)=='5'):
            currentImage=sobelx
        elif (chr(key & 255)=='6'):
            currentImage=sobely

        #display an image based on the key press above
        cv2.imshow(WINDOW_NAME,currentImage)
        #display some helper text
        cv2.putText(currentImage,'1. Loaded Image',(0,25), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)
        cv2.putText(currentImage,'2. Grey Scale',(0,55), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)
        cv2.putText(currentImage,'3. Blurred Image',(0,85), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)
        cv2.putText(currentImage,'4. Laplacian Filter',(0,115), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)
        cv2.putText(currentImage,'5. Sobel X Filter',(0,145), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)
        cv2.putText(currentImage,'6. Sobel Y Filter',(0,175), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0),2)

    #destroy window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
