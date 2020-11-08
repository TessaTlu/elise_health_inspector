from tensorflow.keras import models
import numpy as np
import matplotlib.pyplot as plt
import PIL as Image
from PIL import Image
import cv2
import os
from tensorflow import keras
def scan_result(file_name):
    img_size=150
    array=Image.open(file_name)
    person = np.array(array)
    img_arr = person
    model = keras.models.load_model("x_ray_model")
    resized_arr = cv2.resize(img_arr, (img_size, img_size)) 
    resized_arr=resized_arr/255
    resized_arr=resized_arr.reshape(-1, img_size, img_size, 1)
    result = model.predict(resized_arr)
    result =  np.around(result, decimals=0)
    result = int(result)
    return result