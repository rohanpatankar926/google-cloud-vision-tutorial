import os,io
from urllib import response
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
from PIL import Image,ImageDraw,draw
import random

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"/home/data-guy/Desktop/flaskredis/google_cloud_vision/data-engineering-358308-e8acf964f45b.json"

client=vision.ImageAnnotatorClient()
print(dir(client))

def detect_web_entity(img):
    with io.open(os.path.join(img),"rb") as image_file:
        content=image_file.read()
    image=types.Image(content=content)
    response=client.web_detection(image=image)
    web_detection=response.web_detection
    for entity in web_detection.web_entities:
        print(entity.description)
        print(entity.score)
        print("*"*50)

file_name='154.jpg'
folder_path="/home/data-guy/Desktop/flaskredis/google_cloud_vision/"
print(detect_web_entity(os.path.join(folder_path,file_name)))