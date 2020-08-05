# -*- coding: utf-8 -*-
import cv2
# import tensorflow
import numpy as np
from os import path
# from keras.models import load_model
import base64
import io
from PIL import Image

def face_detector(img_np):
    img = cv2.cvtColor(img_np, cv2.COLOR_RGBA2BGR)
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
    face_list=cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=2,minSize=(64,64))
    #顔が１つ検出された時
    if len(face_list) == 1:
        for rect in face_list:
            x,y,width,height=rect
            img = img[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            if img.shape[0]<64:
                continue
            img = cv2.resize(img,(64,64))
        return img, 0
    else:
        return 0, "Sorry, we detect {} face".format(len(face_list))

# def face_classifier(img):
#     b,g,r = cv2.split(img)
#     img = cv2.merge([r,g,b])
#     img = np.array(img)
#     img_array = []
#     img_array.append(img)
#     img_input=np.array(img_array)
#     model = load_model("./FaceRecog.h5")
#     ans = model.predict(img_input)
#     lis = ["齋藤飛鳥","生田絵梨花","西野七瀬","白石麻衣"]
#     iter = np.argmax(ans, axis = None, out = None)
#     name = lis[iter]
#     return name
