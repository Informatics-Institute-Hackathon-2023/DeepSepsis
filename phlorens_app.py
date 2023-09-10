import streamlit as st
import pandas as pd
import keras
from keras.models import load_model
import numpy as np

st.title('PhLORENS App')
st.header('_Physiological Learned Objective Response Emergency Notification System_')

st.subheader('Demo')

model = load_model('model/DeepSepsis.h5')
columns_name = ['Hour', 'HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2',
       'BaseExcess', 'HCO3', 'FiO2', 'pH', 'PaCO2', 'SaO2', 'AST', 'BUN',
       'Alkalinephos', 'Calcium', 'Chloride', 'Creatinine', 'Bilirubin_direct',
       'Glucose', 'Lactate', 'Magnesium', 'Phosphate', 'Potassium',
       'Bilirubin_total', 'TroponinI', 'Hct', 'Hgb', 'PTT', 'WBC',
       'Fibrinogen', 'Platelets', 'Age', 'Gender', 'Unit1', 'Unit2',
       'HospAdmTime', 'ICULOS']

#risk_levels = {0.2: 'Low Sepsis risk', 0.5: 'Medium Sepsis risk'}

def process_patient_data(patient_file, patient_name):
    patient_data = np.loadtxt(patient_file, delimiter=",")
    patient_data = patient_data.reshape(1, *patient_data.shape)
    structured_data = np.empty(1, dtype=list(zip(columns_name, ['f8']*len(columns_name))))
    structured_data[0] = tuple(patient_data.squeeze())
    structured_data
    probability = model.predict(patient_data)
    probability[0][0]
    if probability <= 0.2:
        st.success(f'Low Sepsis risk for {patient_name}!', icon="✅")
    elif probability <= 0.5:
        st.warning(f'Medium Sepsis risk for {patient_name}!', icon="⚠️")
    else:
        st.error(f'High Sepsis risk for {patient_name}!', icon="🚨")

# Button to click Patient A data
if st.button("Patient A", type="primary"):
    process_patient_data("dataset_demo/patient_a.csv", "Patient A")

# Button to click Patient B data
if st.button("Patient B", type="primary"):
    process_patient_data("dataset_demo/patient_b.csv", "Patient B")

# Upload file
st.subheader('Upload csv file with current EHR')
uploaded_file = st.file_uploader("Upload file")
if uploaded_file is not None:
    process_patient_data(uploaded_file, "uploaded patient information")

st.set_option('deprecation.showfileUploaderEncoding', False)
