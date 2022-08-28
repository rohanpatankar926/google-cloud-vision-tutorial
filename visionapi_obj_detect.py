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

def detect_object(img):
    with io.open(os.path.join(img),"rb") as image_file:
        content=image_file.read()
    image=types.Image(content=content)
    response=client.object_localization(image=image)
    localized_object_annotations=response.localized_object_annotations    
    df=pd.DataFrame(columns=["name","score"])
    for object in localized_object_annotations:
        df =df.append(dict(locale=object.name,description=object.score),ignore_index=True)
    print(df)
    pillow_image=Image.open(img)
    for object in localized_object_annotations:
        r,g,b=random.randint(150,255),random.randint(150,255),random.randint(150,255)
        draw_borders(pillow_image,object.bounding_poly,(r,g,b),pillow_image.size,object.name,object.score)
    pillow_image.show()

file_name='154.jpg'
folder_path="/home/data-guy/Desktop/flaskredis/google_cloud_vision/"
print(detect_object(os.path.join(folder_path,file_name)))