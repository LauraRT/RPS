# Standard imports
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)


def color_recognition():
    
    processed = 0

    while processed == 0:
        _, frame = cap.read()

    #countdown until it takes the picture

        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)

    #taking a picture from the camerafeed to analyse

        img_counter = 1
        img_name = "picture_{}.png".format(img_counter)  
        cv2.imwrite(img_name, frame)

        lower_pink = np.array([150,150,0])
        upper_pink = np.array ([180,255,255])
    
    #analysis of the taken picture
    
        gesture = cv2.imread('picture_1.png')
        print("Reading the gesture!")
        img_counter = img_counter + 1

        cv2.imshow('gesture',gesture)
        cv2.waitKey(0)

    #processing the image, to determine the correct number of markers
    #turning the image into hue, saturation, value spectrum - separating the most unusual, strong colour in the image

        hsv = cv2.cvtColor(gesture, cv2.COLOR_BGR2HSV)
        hue ,saturation ,value = cv2.split(hsv)

        gray_image = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('gray_image.png',gray_image)
    
    #thresholding the image - turning the bringht coloured items to white pixels and the rest to black
    #retval, thresholded = cv2.threshold(saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #filtering the image - bluring slightly the image, to get rid of noise
        medianFil = cv2.medianBlur(gray_image,5)


        cv2.imshow('Median Filtered Image',medianFil)
        cv2.waitKey(0)

    #making contours around the detected objects
        contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
        blobs = 0

    #eliminating contours that are too small
        contour_list = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100 :
                contour_list.append(contour)
                blobs = blobs + 1

        cv2.drawContours(gesture, contour_list,  -1, (255,0,0), 2)
        cv2.imshow('Objects Detected',gesture)
        cv2.waitKey(0)
        print ("No. of contours detected is", blobs, "contours.")

    #interpreting the results

        if blobs == 0:
            #time.sleep(2)
            print("No hand gesture detected.")
            processed = 0
        elif blobs == 1:
            #time.sleep(2)
            return 0
            processed = 1
        elif blobs == 2:
            #time.sleep(2)
            return 1
            processed = 1
        elif blobs == 3:
            #time.sleep(2)
            return 2
            processed = 1
        else:
            #time.sleep(2)
            print("Unknown hand gesture.")
            processed = 0

    #waiting for esc key to exit                    
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()

color_recognition()
