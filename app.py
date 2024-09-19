import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
liver_model = pickle.load(open(f'{working_dir}/saved_models/liver_model.sav', 'rb'))
kidney_model = pickle.load(open(f'{working_dir}/saved_models/kidney_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Liver Disease Prediction',
                            'Kidney Disease Prediction',
                            'Heart Disease Prediction',
                            'Diabetes Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'droplet', 'heart', 'person'],
                           default_index=0)

# Liver Disease Prediction Page
if selected == 'Liver Disease Prediction':
    st.title('Liver Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Gender = st.text_input('Gender (0 for Female, 1 for Male)')
    with col3:
        Total_Bilirubin = st.text_input('Total Bilirubin')
    with col1:
        Direct_Bilirubin = st.text_input('Direct Bilirubin')
    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase')
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase')
    with col2:
        Total_Proteins = st.text_input('Total Proteins')
    with col3:
        Albumin = st.text_input('Albumin')
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')

    liver_diagnosis = ''

    if st.button('Liver Disease Test Result'):
        user_input = [Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                      Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Proteins,
                      Albumin, Albumin_and_Globulin_Ratio]
        user_input = [float(x) for x in user_input]
        liver_prediction = liver_model.predict([user_input])

        if liver_prediction[0] == 1:
            liver_diagnosis = 'The person has liver disease'
        else:
            liver_diagnosis = 'The person does not have liver disease'

    st.success(liver_diagnosis)

# Kidney Disease Prediction Page
if selected == 'Kidney Disease Prediction':
    st.title('Kidney Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Blood_Pressure = st.text_input('Blood Pressure')
    with col3:
        Specific_Gravity = st.text_input('Specific Gravity')
    with col1:
        Albumin = st.text_input('Albumin')
    with col2:
        Sugar = st.text_input('Sugar')
    with col3:
        Red_Blood_Cells = st.text_input('Red Blood Cells (0 for Normal, 1 for Abnormal)')
    with col1:
        Pus_Cell = st.text_input('Pus Cell (0 for Normal, 1 for Abnormal)')
    with col2:
        Pus_Cell_Clumps = st.text_input('Pus Cell Clumps (0 for Not Present, 1 for Present)')
    with col3:
        Bacteria = st.text_input('Bacteria (0 for Not Present, 1 for Present)')
    with col1:
        Blood_Glucose_Random = st.text_input('Blood Glucose Random')
    with col2:
        Blood_Urea = st.text_input('Blood Urea')
    with col3:
        Serum_Creatinine = st.text_input('Serum Creatinine')
    with col1:
        Sodium = st.text_input('Sodium')
    with col2:
        Potassium = st.text_input('Potassium')
    with col3:
        Hemoglobin = st.text_input('Hemoglobin')
    with col1:
        Packed_Cell_Volume = st.text_input('Packed Cell Volume')
    with col2:
        White_Blood_Cell_Count = st.text_input('White Blood Cell Count')
    with col3:
        Red_Blood_Cell_Count = st.text_input('Red Blood Cell Count')

    kidney_diagnosis = ''

    if st.button('Kidney Disease Test Result'):
        user_input = [Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar,
                      Red_Blood_Cells, Pus_Cell, Pus_Cell_Clumps, Bacteria,
                      Blood_Glucose_Random, Blood_Urea, Serum_Creatinine,
                      Sodium, Potassium, Hemoglobin, Packed_Cell_Volume,
                      White_Blood_Cell_Count, Red_Blood_Cell_Count]
        user_input = [float(x) for x in user_input]
        kidney_prediction = kidney_model.predict([user_input])

        if kidney_prediction[0] == 1:
            kidney_diagnosis = 'The person has kidney disease'
        else:
            kidney_diagnosis = 'The person does not have kidney disease'

    st.success(kidney_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
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

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
                      oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
