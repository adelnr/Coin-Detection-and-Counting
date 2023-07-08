import cv2
import cvzone
import numpy as np

cap = cv2.VideoCapture(2)
cap.set(3,640)
cap.set(4,480)

totalmoney = 0






def empty(a):
    pass
cv2.namedWindow("settings")
cv2.resizeWindow("settings",640,240)
cv2.createTrackbar("Threshold1","settings",219,255,empty)
cv2.createTrackbar("Threshold2","settings",233,255,empty)

def preprocessing(img):

    imgpre = cv2.GaussianBlur(img,(5,5),2)
    thresh1 = cv2.getTrackbarPos("Threshold1","settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "settings")
    imgpre = cv2.Canny(imgpre,thresh1,thresh2)
    kernel = np.ones((3,3),np.uint8)
    imgpre = cv2.dilate(imgpre,kernel,iterations=1)
    imgpre = cv2.morphologyEx(imgpre,cv2.MORPH_CLOSE,kernel)

    return imgpre
while True:
    success, img = cap.read()
    imgpre = preprocessing(img)
    imgcontours ,confound = cvzone.findContours(img,imgpre,minArea=20)
    totalmoney = 0
    imgcount = np.zeros((480, 640, 3), np.uint8)

    if confound:
        for count,contour in enumerate (confound):
            peri = cv2.arcLength(contour['cnt'], True)
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)
            if len(approx)>5:
                area = (contour['area'])

                if area<1500:
                    totalmoney+=1

                elif 1600<area<1990:
                    totalmoney+=2

                else:
                    totalmoney+=5

    print(totalmoney)

    cvzone.putTextRect(imgcount, f'Cent.{totalmoney}', (100, 150),scale=5,offset=30,thickness=5)
    imggstacked = cvzone.stackImages([img,imgpre,imgcontours,imgcount],2,1)
    cvzone.putTextRect(imggstacked, f'Cent.{totalmoney}',(50, 50))
    cv2.imshow("Image",imggstacked)

    cv2.waitKey(1)

