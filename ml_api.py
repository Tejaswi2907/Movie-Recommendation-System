# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:30:17 2023

@author: USER
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from fastapi import FastAPI, File, UploadFile
# load the saved model
asr = pickle.load(open('asr.sav', 'rb'))
app = FastAPI()


@app.post("/")
async def upload_audio(audio: UploadFile = File(...)):
    contents = await audio.read()
    # Process the audio contents here
    return {"file_name": audio.filename}

'''
@app.post('/')
def asr_pred():
    # input_data=input_parameters.json()
    prediction = asr.predict()
    print(prediction)
'''