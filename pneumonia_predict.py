from tensorflow.keras import models
import numpy as np
import matplotlib.pyplot as plt
import PIL as Image
from PIL import Image
import cv2
import os
from tensorflow import keras
def scan_result(file_name):
    img_size=150  ### ширина и высота картинки 
    array=Image.open(file_name) 
    array=np.array(array)
    ### Делаем картинку черно-белой, если она цветная
    if(len(array.shape)==3):
        grayImage = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY) 
        array=grayImage
    person = np.array(array)
    img_arr = person

    ### Загружаем модель
    model = keras.models.load_model("x_ray_model")

    ### Меняем размер картинки
    resized_arr = cv2.resize(img_arr, (img_size, img_size)) 
    resized_arr=resized_arr/255
    resized_arr=resized_arr.reshape(-1, img_size, img_size, 1)

    ### Строим предположение с помощью ранее обученной модели
    result = model.predict(resized_arr)
    result =  np.around(result, decimals=0)
    result = int(result)
    return result