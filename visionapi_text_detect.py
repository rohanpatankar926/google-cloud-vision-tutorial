import os,io
from urllib import response
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"/home/data-guy/Desktop/flaskredis/google_cloud_vision/data-engineering-358308-e8acf964f45b.json"

client=vision.ImageAnnotatorClient()
print(dir(client))

def detect_text(img):
    with io.open(os.path.join(img),"rb") as image_file:
        content=image_file.read()

    image=types.Image(content=content)
    response=client.text_detection(image=image)

    text=response.text_annotations
    df=pd.DataFrame(columns=["loacale","description"])

    for tex in text:
        df =df.append(dict(locale=tex.locale,description=tex.description),ignore_index=True)
    return df


file_name='154.jpg'
folder_path="/home/data-guy/Desktop/flaskredis/google_cloud_vision/"
print(detect_text(os.path.join(folder_path,file_name)))