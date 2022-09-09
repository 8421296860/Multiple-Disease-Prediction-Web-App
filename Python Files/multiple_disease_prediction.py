# -*- coding: utf-8 -*-
"""
created by - Bhushan Deshmukh
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Diabetes Prediciton Page
def diabetes_prediction(diabetes_model):
    #Page Title
    st.title('Diabetes Prediction')
    
    #Getting input data from the user
    
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1: 
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
        
    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabeted Prediction Function')
    
    with col2:
        Age = st.text_input('Age')
    
    #Code for prediction
    diabetes_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Diabetes Test Result'):
        
        diabetes_predicted = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                             Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diabetes_predicted[0] == 0): 
            diabetes_diagnosis = 'The person is Not Diabetic.'
        else:
            diabetes_diagnosis = 'The person is Diabetic.'
        
    st.success(diabetes_diagnosis)
    
    
#Heart Disease Prediciton Page
def heart_disease_prediction(heart_disease_model):
    #Page Title
    st.title('Heart Disease Prediction')
    
    #Getting input data from the user
    
    #Columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Sex = st.text_input('Gender')
        
    with col3:
        CP = st.text_input('Chest Pain Type')
        
    with col1:
        Trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        Chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        FBS = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        Restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        Thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        Exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        Oldpeak = st.text_input('ST Depression Induced by Exercise')
        
    with col2:
        Slope = st.text_input('Slope of the Peak Exercise ST Segment')
        
    with col3:
        CA = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        Thal = st.text_input('Defect Type')

    #Code for prediction
    heart_disease_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Heart Disease Test Result'):
    
        heart_disease_predicted = heart_disease_model.predict([[Age,Sex,CP,Trestbps,Chol,FBS,Restecg,Thalach,Exang,Oldpeak,Slope,CA,Thal]])           
        
        if (heart_disease_predicted[0] == 1):
          heart_disease_diagnosis = 'The person is having heart disease'
        else:
          heart_disease_diagnosis = 'The person does not have any heart disease'
          
        print(heart_disease_diagnosis)
        
    st.success(heart_disease_diagnosis)
    
    
#Parkinsons Prediciton Page
def parkinsons_prediction(parkinsons_disease_model):
    #Page Title
    st.title('Parkinsons Prediction')
    
    #Getting input data from the user
    
    #Columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        Fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        Flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_Perc = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
    
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    #Code for prediction
    parkinsons_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Parkinsons Test Result'):
    
        parkinsons_prediction = parkinsons_disease_model.predict([[Fo, Fhi, Flo, Jitter_Perc, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, 
                                                                      APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])           
        
        if (parkinsons_prediction[0] == 0):
          parkinsons_diagnosis = 'The person is Healthy.\n'
        else:
          parkinsons_diagnosis = 'The person is Parkinson\'s Positive.\n'
        
    st.success(parkinsons_diagnosis)
    
    
#Breast Cancer Prediciton Page
def breast_cancer_prediction(breast_cancer_model):
    #Page Title
    st.title('Breast Cancer Prediction')
    
    #Getting input data from the user
    
    #Columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
        
    with col2:
        texture_mean = st.text_input('Texture Mean')
        
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')
        
    with col4:
        area_mean = st.text_input('Area Mean')
        
    with col5:
        smoothness_mean = st.text_input('Smoothness Mean')
        
    with col1:
        compactness_mean = st.text_input('Compactness Mean')
        
    with col2:
        concavity_mean = st.text_input('Concavity Mean')
        
    with col3:
        concave_points_mean = st.text_input('Concave Points Mean')
        
    with col4:
        symmetry_mean = st.text_input('Symmetry Mean')
        
    with col5:
        fractal_dimension_mean = st.text_input('Fractal Dim. Mean')
        
    with col1:
        radius_se = st.text_input('Radius SE')
        
    with col2:
        texture_se = st.text_input('Texture SE')
        
    with col3:
        perimeter_se = st.text_input('Perimeter SE')
        
    with col4:
        area_se = st.text_input('Area SE')
        
    with col5:
        smoothness_se = st.text_input('Smoothness SE')
        
    with col1:
        compactness_se = st.text_input('Compactness SE')
        
    with col2:
        concavity_se = st.text_input('Concavity SE')
        
    with col3:
        concave_points_se = st.text_input('Concave Points SE')
    
    with col4:
        symmetry_se = st.text_input('Symmetry SE')
        
    with col5:
        fractal_dimension_se = st.text_input('Fractal Dim. SE')
        
    with col1:
        radius_worst = st.text_input('Radius Worst')
        
    with col2:
        texture_worst = st.text_input('Texture Worst')
        
    with col3:
        perimeter_worst = st.text_input('Perimeter Worst')
        
    with col4:
        area_worst = st.text_input('Area Worst')
        
    with col5:
        smoothness_worst = st.text_input('Smoothness Worst')
        
    with col1:
        compactness_worst = st.text_input('Compactness Worst')
        
    with col2:
        concavity_worst = st.text_input('Concavity Worst')
        
    with col3:
        concave_points_worst = st.text_input('Concave Points Worst')
    
    with col4:
        symmetry_worst = st.text_input('Symmetry Worst')
        
    with col5:
        fractal_dimension_worst = st.text_input('Fractal Dim. Worst')
        
    #Code for prediction
    breast_cancer_diagnosis = ''
    
    #Creating a button for prediction
    if st.button('Breast Cancer Test Result'):
    
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,
                                                                   compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,
                                                                   fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,
                                                                   smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,
                                                                   fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,
                                                                   smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,
                                                                   symmetry_worst,fractal_dimension_worst]])           
        
        if (breast_cancer_prediction[0] == 'M'): 
            breast_cancer_diagnosis = 'The person is having Malignant Breast Cancer.\n'
        else:
            breast_cancer_diagnosis = 'The person is having Benign Breast Cancer.\n'
        
    st.success(breast_cancer_diagnosis)
    

def main():
    #Loading the saved model
    diabetes_model = pickle.load(open('diabetes_trained_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_trained_model.sav', 'rb'))
    parkinsons_disease_model = pickle.load(open('parkinsons_disease_trained_model.sav', 'rb'))
    breast_cancer_model = pickle.load(open('breast_cancer_trained_model.sav', 'rb'))
    
    #Sidebar for navigation
    with st.sidebar:
        selected = option_menu('Multiple Disease Predicition System',
                               ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Prediction',
                                'Breast Cancer Prediction'],
                               icons = ['activity', 'heart', 'person', 'gender-female'],
                               default_index = 0)
    
    if(selected == 'Diabetes Prediction'):
        diabetes_prediction(diabetes_model)
        
    if (selected == 'Heart Disease Prediction'):
        heart_disease_prediction(heart_disease_model)
        
    if (selected == 'Parkinsons Prediction'):
        parkinsons_prediction(parkinsons_disease_model)
    
    if (selected == 'Breast Cancer Prediction'):
        breast_cancer_prediction(breast_cancer_model)

if __name__ == '__main__':
    
    main()
