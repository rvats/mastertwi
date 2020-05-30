"""
@Author: Rahul Vats
@AuthorEmail: vats.rahul@gmail.com
@Purpose: This algorithm recognizes a face, runs a security check
and engages in a simulated conversation.
@History:
"""
# import the opencv module for getting support on face recognition and camera operations
import cv2
# import the speech to text module
import pyttsx3
# import the speech to text module
import sys

import logging as log

import datetime as dt

import configparser

import Greetings 

from datetime import time
from time import sleep

# Get user supplied values Will
# imagePath = sys.argv[1]

# Initialize the Speech Engine
engine = pyttsx3.init()

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('SecurityGreeterConfig.ini', 'w') as configfile:
    config.write(configfile)

# Define the face recognition model and Create the haar cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image for security authorization
# image = cv2.imread(imagePath)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
"""
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
"""

# Set Initial Variables Here
# Set a variable to check and greet for the first time
greeted = False

# Initialize Logging
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if not greeted:
        greeting = Greetings.GetGreetingMessage()
        engine.say(greeting)
        # Tell the engine to start saying what you wanted it to and stop when it reaches the end of the queued sayings.
        engine.runAndWait()
        greeted = True


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
