
import cv2 # Importing the OpenCV module
from cvzone.HandTrackingModule import HandDetector # Importing the HandTrackingModule from cvzone
import socket # Importing the socket module

#Parameters

width , height = 1280, 720

#Webcam

# URL del feed video dell'IP Webcam
url = "http://192.168.10.101:8080/video"

# Apre il feed video
#cap = cv2.VideoCapture(url) # Capturing the video from the Huaweii webcam using IP Webcam

cap = cv2.VideoCapture(0) # Capturing the video from the webcam
cap.set(3, width) # Setting the width of the video
cap.set(4, height) # Setting the height of the video

# Hand Tracking

detector = HandDetector(maxHands=1 , detectionCon=0.8) # Creating an object of HandDetector class

# Socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# Creating a socket object

server_address = ("127.0.0.1", 5052) # Setting the server address





while True:
    success, img = cap.read() # Reading the video from the webcam
    hands, img = detector.findHands(img) # Finding the hands in the video
    data=[] # Creating an empty list to store the data of the landmarks of the hand

    if hands:
        hand1 = hands[0]# Getting the first hand
        lmList1 = hand1["lmList"]# Getting the list of landmarks of the first hand
        for lm in lmList1:
            data.extend([lm[0],height-lm[1], lm[2]]) # Appending the landmarks of the hand to the data list
        #print(data)
        sock.sendto(str.encode(str(data)), server_address) # Sending the data to the server
        




    img = cv2.resize(img , (0,0) , None , 0.5 , 0.5) # Resizing the video
    cv2.imshow("Image", img) # Displaying the video
    cv2.waitKey(1) # Waiting for the key to be pressed






