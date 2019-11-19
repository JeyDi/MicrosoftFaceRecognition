import asyncio, io, glob, os, sys, time, uuid, requests
from urllib.parse import urlparse
from io import BytesIO
import sys
import datetime
import cv2
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType, APIErrorException


def auth_client(key=None,endpoint=None):
    """Authenticate the client"""

    if(key is None):
        print("Cognitive Service Key not found, modify the config.yml file")
        sys.exit("Impossibile to use the program without correct configuration")
    if(endpoint is None):
        print("Cognitive Service Endpoint not found, modify the config.yml file")
        sys.exit("Impossibile to use the program without correct configuration")

    # Create an authenticated FaceClient
    try:
        face_client = FaceClient(endpoint, CognitiveServicesCredentials(key))
    except:
        print("Impossible to auth to the service..please fix or retry..")
    
    return face_client


def detect(face_client,video_frame_buffer):
    """Detect info by an image from the camera"""

    #img = cv2.imencode('.jpg', image)[1].tostring()

    video_frame_stream = BytesIO(video_frame_buffer.tobytes())

    try:
        detected = face_client.face.detect_with_stream(video_frame_stream)
        
        image_recognized = detected.json()
        
        image_caption = image_recognized["description"]["captions"][0]["text"].capitalize()
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = time_now + ": " + image_caption

    except APIErrorException as api_error:
        print(api_error.message)
        result = "Error"
    
    return result