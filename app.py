import pickle
import streamlit as st
import pandas as pd
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title('Kidney Disease Predictor 👨‍⚕️')

col1, spacer, col2 = st.columns([3, 0.1, 3])

with col1:
    age = st.text_input("Enter the Age : ")
    blood_pressure = st.slider('Blood_pressure : ',30,200)
    specific_gravity = st.radio('Specific_gravity : ', [1.005, 1.010, 1.015, 1.020 ,1.025], horizontal=True) ##
    albumin = st.radio('Albumin level: ',[0,1,2,3,4,5], horizontal=True) ##
    sugar = st.radio('Sugar level: ',[0,1,2,3,4,5], horizontal=True) ##

    blood_glucose_random = st.slider('Blood_glucose_random : ',20,500)
    blood_urea = st.slider('Blood_urea : ',30,200)
    serum_creatinine = st.slider('Serum_creatinine : ',1,400)

    red_blood_cells = st.radio('Red_blood_cells type', ['normal','abnormal'], horizontal=True)
    pus_cell = st.radio('Pus_cell type', ['normal','abnormal'], horizontal=True)
    pus_cell_clumps = st.radio('Choose whether pus cell clumps are present', ['notpresent', 'present'], horizontal=True)
    bacteria = st.radio('Choose whether bacteria is present', ['notpresent', 'present'], horizontal=True)


with spacer:
    pass

with col2:

    sodium = st.slider('Sodium : ',0,100)
    potassium = st.slider('Potassium : ',4,200)
    haemoglobin = st.slider('Haemoglobin : ',2,20)
    packed_cell_volume = st.slider('Packed_cell_volume : ',5,70)
    white_blood_cell_count = st.slider('White_blood_cell_count : ',2000,30000)
    red_blood_cell_count = st.slider('Red_blood_cell_count : ',1,10)

    hypertension = st.radio('Is hypertension present?', ['yes', 'no'], horizontal=True)
    diabetes_mellitus = st.radio('Is diabetes_mellitus present?', ['yes', 'no'], horizontal=True)
    coronary_artery_disease = st.radio('Is coronary_artery_disease present?', ['yes', 'no'], horizontal=True)
    appetite = st.radio('How is the appetite?', ['good', 'poor'], horizontal=True)
    peda_edema = st.radio('Is peda_edema present?', ['yes', 'no'], horizontal=True)
    anemia = st.radio('Is anemia present?', ['yes', 'no'], horizontal=True)


def prediction():
    input = [[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, anemia]]
    k = model.predict(input)
    proba = model.predict_proba(input)

    if k == 1:
        st.markdown(f'<div style="background-color: #FF0000; padding: 10px; ">The patient has Kidney disease. Prediction accuracy: {proba[0][1]*100:.2f}%</div>', unsafe_allow_html=True)
    elif k == 0:
        st.markdown(f'<div style="background-color: #0F951C; padding: 10px; ">The patient does not have Kidney disease. Prediction accuracy: {proba[0][0]*100:.2f}%</div>', unsafe_allow_html=True)

if st.button('Predict the kidney disease', on_click=prediction):
    # Scroll to the top after button click
    js_scroll_top = '''
    <script>
        var body = window.parent.document.querySelector(".main");
        body.scrollTop = 0;
    </script>
    '''
    st.components.v1.html(js_scroll_top)

    st.write("\n\n")