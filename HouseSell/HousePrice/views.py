from django.shortcuts import render
from django.contrib import messages

import os
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# Create your views here.

def home(request):
    messages.success(request, 'Hello welcome here you can accurate your home values')
    return render(request, 'HousePrice/home.html')

def predict(request):
    return render(request, 'HousePrice/predict.html')

def result(request):
    data = pd.read_csv(r'ADAMA_house_prices_dataset.csv')
    data = data.drop(['location'], axis=1)
    X = data.drop('price', axis= 1)
    Y = data['price']
    X_train, X_test,Y_train,Y_test = train_test_split(X, Y, test_size= .30)
    model = LinearRegression() 
    model.fit(X_train, Y_train) 
  
    var1 = float(request.GET['n1']) 
    var2 = float(request.GET['n2']) 
    var3 = float(request.GET['n3']) 
    var4 = float(request.GET['n4']) 
    var5 = float(request.GET['n5']) 


    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1)) 
  
    pred = round(pred[0]) 
  
    price = "The Predicted Rent Is Rs "+str(pred) 
    return render(request, 'HousePrice/predict.html', {"result2":price})
