# -*- coding: utf-8 -*-

# Keras Library - https://keras.io/
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.models import load_model

# Array Library - https://numpy.org/doc/stable/
from numpy import expand_dims, argmax, sum

# Built-in Library
from time import time as ti

def processor(img_path:str, model_path:str='./brain-tumor.h5')->str:
    '''
    Load the model and process the image.
        
        Parameters:
            img_path: str
                Path of the image file.
            model_path: str
                Path of the keras model(default: ./brain-tumor.h5)
        Returns:
            probabilities: dict
                All labels and probabilities.
            timer:
                Model processing time.
    '''
    
    model = load_model(model_path)
    
    labels:list = ['glioma', 'meningioma', 'normal', 'adenoma']
    
    image = load_img(img_path, target_size=(224,224))
    
    image = img_to_array(image)
    
    image = expand_dims(image,axis=0)
    
    first = ti()
    
    result = model.predict(image/255.0,verbose=0)
    
    timer = f'{first - ti():.2f}'
    
    total = sum(result)
    
    probabilities:dict = {
        'glioma':f'{(result[0][0]/total)*100:.2f}%',
        'meningioma':f'{(result[0][1]/total)*100:.2f}%',
        'normal':f'{(result[0][2]/total)*100:.2f}%',
        'adenoma':f'{(result[0][3]/total)*100:.2f}%'
    }
    
    return probabilities, timer
    