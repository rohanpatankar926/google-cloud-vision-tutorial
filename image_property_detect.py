import os 
from google.cloud import vision
import io
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/dataguy/cloudvisionapi/auth-xxxxxxxxxxxx.json"
client=vision.ImageAnnotatorClient()

def image_property_detector(filename= input("please enter image file name-->")):
    image_path= f"/home/dataguy/cloudvisionapi/images/{filename}"

    with io.open(image_path,"rb") as image_file:
        content=image_file.read()

    image=vision.types.Image(content=content)
    response=client.image_properties(image=image).image_properties_annotations

    dominant_colors=response.dominant_colors

    for color in dominant_colors:
        print("pixel function: {}".format(color.pixel_fraction))
        print("score: {}".format(color.score))
        print("color red: {}".format(color.color.red))
        print("color green: {}".format(color.color.green))
        print("blue: {}".format(color.color.blue))
        print("\n")

if __name__=="__main__":
    res=image_property_detector()
    print(res)
