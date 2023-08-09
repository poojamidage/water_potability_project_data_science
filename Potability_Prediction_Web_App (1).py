# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:03:09 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Water_Potability_Model.sav','rb'))


#creating a function for prediction

def potability_prediction(Input_data):
    
    
    #changing Input_data to numpy array
    Input_data_as_numpy_array = np.asarray(Input_data)
    
    #Reshaping the array as we are predicting for one instance
    Input_data_reshaped = Input_data_as_numpy_array.reshape(1,-1)
    
    Prediction = loaded_model.predict(Input_data_reshaped)
    print(Prediction)

    if (Prediction[0]==0):
        return'Water is not potable'
    else :
        return'Water is potable'
        
        
def main():
    
    #giving a title
    st.title('Potability_Prediction_Web_App')
    
    #getting the input data from user
    
    
    ph = st.text_input('value of ph')
    Hardness = st.text_input('Hardness level')
    Solids = st.text_input('count of Solids')
    Chloramines = st.text_input('value of Chloramines')
    Sulfate = st.text_input('value of Sulfate')
    Conductivity = st.text_input('Conductivity')
    Organic_carbon = st.text_input('value of Organic_carbon')
    Trihalomethanes = st.text_input('value of Trihalomethanes')
    Turbidity = st.text_input('value of Turbidity')
    
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Potability Test Result'):
        diagnosis = potability_prediction([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity])


    st.success(diagnosis)
    
    
 
if __name__ == '__main__':
    main()