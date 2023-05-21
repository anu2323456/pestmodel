from joblib import load
from django.shortcuts import render
from keras.utils import load_img, img_to_array
from skimage.transform import resize
from skimage.io import imread
import sklearn
import cv2
from django.core.files.storage import FileSystemStorage
from keras.preprocessing import image
loadmodel=load(r'C:\Users\hp\Documents\pestdetection\pestdetection\pest\savedmodel\pestmodels.joblib')

from PIL import Image, ImageOps
import numpy as np

# Create your views here.

# def index(request):
#     return render(request,'index.html')

def predict(request):
    pred=None
    y=None
    x=None
    if request.method=='POST':
        image=request.FILES['image']
        fs=FileSystemStorage()
        filepathname=fs.save(image.name,image)
        filepathname=fs.url(filepathname)
        testimage='.'+filepathname
        print(testimage)
        image=imread(testimage)
        imgresize=resize(image,(150,150,3))
        x=imgresize.flatten().reshape(1,-1)
        
        
        print('resized array is',x)

        y=loadmodel.predict(x)
        pred=y
        print('output is',pred)
        


        if pred == [0]:
            pred='aphids'

        if pred == [1]:
            pred='armyworm'
        if pred == [2]:
            pred='beetle'

        if pred == [3]:
            pred='bollworm'

        if pred == [4]:
            pred='grasshopper'


        if pred ==[5]:
            pred='mites'

        if pred == [6]:
             pred='mosquito'

        if pred == [7]:
             pred='sawfly'

        if pred == [8]:
             pred='stem_borer'
        y=0




    return render(request,'home.html',{'pred':pred})