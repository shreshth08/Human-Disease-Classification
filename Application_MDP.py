#!/usr/bin/env python
# coding: utf-8



import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Human Disease Prediction Application",layout='wide',page_icon="💖")

diabetes_model = pickle.load(open('C:/Users/820sh/diabetes_knn.pkl','rb'))
kidney_diesease_model = pickle.load(open('C:/Users/820sh/kindey_dtc.pkl','rb'))
liver_diesease_model = pickle.load(open('C:/Users/820sh/liver.pkl','rb'))
heart_disease_model = pickle.load(open('C:/Users/820sh/heart.pkl','rb'))


with st.sidebar:
    selected = option_menu("Human Disease Prediction Application", 
                ['Diabetes Prediction',
                 'Heart Disease Prediction',
                 'Kidney Disease Prediction',
'Liver Disease Prediction'],
                 menu_icon='hospital-fill',
                 icons=['activity','heart', 'person','heart'],
                 default_index=0)

if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("BloodPressure Value")
    with col1:
        SkinThickness = st.text_input("SkinThickness Value")
    with col2:
        Insulin = st.text_input("Insulin Value")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction Value")
    with col2:
        Age = st.text_input("Age")
    diabetes_result = ""
    if st.button("Diabetes Test Result"):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                    BMI,DiabetesPedigreeFunction,Age]
        
        user_input = [float(x) for x in user_input]
        prediction = diabetes_model.predict([user_input])
        if prediction[0]==1:
            diabetes_result = "The person has diabetic"
        else:
            diabetes_result = "The person has no diabetic"
    st.success(diabetes_result)

if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction Using Machine Learning")
    col1, col2, col3  = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain Types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestroal in mg/dl")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    heart_disease_result = ""
    if st.button("Heart Disease Test Result"):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])
        if prediction[0]==1:
            heart_disease_result = "This person is having heart disease"
        else:
            heart_disease_result = "This person does not have any heart disease"
    st.success(heart_disease_result)
    
if selected == 'Kidney Disease Prediction':
    
    st.title("Kidney Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.text_input('Age')

    with col2:
        blood_pressure = st.text_input('Blood Pressure')

    with col3:
        specific_gravity = st.text_input('Specific Gravity')

    with col4:
        albumin = st.text_input('Albumin')

    with col5:
        sugar = st.text_input('Sugar')

    with col1:
        red_blood_cells = st.text_input('Red Blood Cell')

    with col2:
        pus_cell = st.text_input('Pus Cell')

    with col3:
        pus_cell_clumps = st.text_input('Pus Cell Clumps')

    with col4:
        bacteria = st.text_input('Bacteria')

    with col5:
        blood_glucose_random = st.text_input('Blood Glucose Random')

    with col1:
        blood_urea = st.text_input('Blood Urea')

    with col2:
        serum_creatinine = st.text_input('Serum Creatinine')

    with col3:
        sodium = st.text_input('Sodium')

    with col4:
        potassium = st.text_input('Potassium')

    with col5:
        haemoglobin = st.text_input('Haemoglobin')

    with col1:
        packed_cell_volume = st.text_input('Packet Cell Volume')

    with col2:
        white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col3:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col4:
        hypertension = st.text_input('Hypertension')

    with col5:
        diabetes_mellitus = st.text_input('Diabetes Mellitus')

    with col1:
        coronary_artery_disease = st.text_input('Coronary Artery Disease')

    with col2:
        appetite = st.text_input('Appetitte')

    with col3:
        peda_edema = st.text_input('Peda Edema')
    with col4:
        aanemia = st.text_input('Aanemia')

    # code for Prediction
    kindey_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Kidney's Test Result"):

        user_input = [age, blood_pressure, specific_gravity, albumin, sugar,
       red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
       blood_glucose_random, blood_urea, serum_creatinine, sodium,
       potassium, haemoglobin, packed_cell_volume,
       white_blood_cell_count, red_blood_cell_count, hypertension,
       diabetes_mellitus, coronary_artery_disease, appetite,
       peda_edema, aanemia]

        user_input = [float(x) for x in user_input]

        prediction = kidney_diesease_model.predict([user_input])

        if prediction[0] == 1:
            kindey_diagnosis = "The person has Kidney's disease"
        else:
            kindey_diagnosis = "The person does not have Kidney's disease"
    st.success(kindey_diagnosis)

if selected == 'Liver Disease Prediction':
    
    st.title("Liver Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input("Age")
    with col2:
        Gender = st.text_input("Gender")
    with col3:
        Total_Bilirubin = st.text_input("Total Bilirubin")
    with col1:
        Direct_Bilirubin = st.text_input("direct Bilirubin")
    with col2:
        Alkaline_Phosphotase = st.text_input("Alkaline Phosphotase")
    with col3:
        Alamine_Aminotransferase = st.text_input("Alamine Aminotransferse")
    with col1:
        Aspartate_Aminotransferase = st.text_input("Aspartate Aminotransferse")
    with col2:
        Total_Protiens = st.text_input("Total Proteins")
    with col3:
        Albumin = st.text_input("Albumin")
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input("Ratio of Albumin and Globulin")
    

    # code for Prediction
    liver_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Liver's Test Result"):

        user_input = [Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
                     Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]

        user_input = [float(x) for x in user_input]

        prediction = liver_diesease_model.predict([user_input])

        if prediction[0] == 1:
            liver_diagnosis = "The person has Liver's disease"
        else:
            liver_diagnosis = "The person does not have Liver's disease"
    st.success(liver_diagnosis)
