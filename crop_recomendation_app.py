# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 22:48:50 2022

@author: M_ISHFAQ
"""

import numpy as np
import pickle
import streamlit as st



#loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

# creating a function for Prediction

def Crop_Recomendation(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return(prediction)

#Crop Prediction Page

   
def main():
    # title
   
    st.title('Crop Recomendation by Land Gredient')
    # getting the data from the users
    

    N=(st.text_input('Quantity of Nitrogen'))
    P=(st.text_input('Quantity of Phosphorus'))
    K=(st.text_input('Quantity of Potasiam'))
    temprature=(st.text_input('Level of Temprature'))
    humidity=(st.text_input('Level of Humidity'))
    ph=(st.text_input('Level of PH'))
    Rainfall=(st.text_input('Rainfall in ML'))
    
    
    #code for Prediction
    Recomendation=''
    
    
    
    
    # creating a button for prediction
    if st.button('Recomended Crop'):
        Recomendation= Crop_Recomendation([N, P, K, temprature, humidity, ph, Rainfall])
    
    st.success(Recomendation)
    


    
if __name__ == '__main__':
    main()
st.title('Developed By:    Muhammad Ishfaq')
