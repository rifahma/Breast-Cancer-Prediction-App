import streamlit as st
import joblib 
import pandas as pd

# Set page config for mobile responsiveness
st.set_page_config(page_title="Breast Cancer Diagnosis Prediction App", layout="wide")

# Load the model
model = joblib.load('breast_cancer_model.pkl')

st.title('Breast Cancer Diagnosis Prediction App')

st.write("""
### Answer the following questions to get a prediction and get personalized suggestion based on what you have input:
""")

# Sidebar for user inputs
st.sidebar.header('User Input Parameters')

# Question: Personal and family medical record
diagnosed_cancer = st.sidebar.radio('Have you ever been diagnosed with breast cancer or any other type of cancer before?', ['No', 'Yes'])
previous_biopsies = st.sidebar.radio('Have you had any previous breast biopsies or surgeries?', ['No', 'Yes'])
family_history = st.sidebar.radio('Do you have a family history of breast cancer (e.g., mother, sister, daughter)?', ['No', 'Yes'])

# Question: Symptoms and Physical Changes
lumps_changes = st.sidebar.radio('Have you noticed any lumps or changes in your breast tissue?', ['No', 'Yes'])
pain_tenderness = st.sidebar.radio('Have you experienced any pain or tenderness in your breasts?', ['No', 'Yes'])
nipple_discharge = st.sidebar.radio('Do you have any nipple discharge or changes in the appearance of your nipples?', ['No', 'Yes'])
size_shape_changes = st.sidebar.radio('Have you observed any changes in the size, shape, or appearance of your breasts?', ['No', 'Yes'])
skin_changes = st.sidebar.radio('Have you noticed any skin changes on your breasts, such as dimpling or redness?', ['No', 'Yes'])

# Question: Screening and Preventive Measures
mammogram = st.sidebar.radio('Have you had a mammogram before, and if so, when was your last one?', ['No', 'Yes'])
other_screening = st.sidebar.radio('Have you undergone any other breast cancer screening tests, such as MRI or ultrasound?', ['No', 'Yes'])

# Convert responses to numerical values
diagnosed_cancer = 1 if diagnosed_cancer == 'Yes' else 0
previous_biopsies = 1 if previous_biopsies == 'Yes' else 0
family_history = 1 if family_history == 'Yes' else 0
lumps_changes = 1 if lumps_changes == 'Yes' else 0
pain_tenderness = 1 if pain_tenderness == 'Yes' else 0
nipple_discharge = 1 if nipple_discharge == 'Yes' else 0
size_shape_changes = 1 if size_shape_changes == 'Yes' else 0
skin_changes = 1 if skin_changes == 'Yes' else 0
mammogram = 1 if mammogram == 'Yes' else 0
other_screening = 1 if other_screening == 'Yes' else 0

# Create a Dataframe for input features
input_data = pd.DataFrame({
    'diagnosed_cancer': [diagnosed_cancer],
    'previous_biopsies': [previous_biopsies],
    'family_history': [family_history],
    'lumps_changes': [lumps_changes],
    'pain_tenderness': [pain_tenderness],
    'nipple_discharge': [nipple_discharge],
    'size_shape_changes': [size_shape_changes],
    'skin_changes': [skin_changes],
    'mammogram': [mammogram],
    'other_screening': [other_screening]
})

# Predict button
if st.button('Get Prediction'):
    prediction = model.predict(input_data)
    diagnosis = 'Malignant' if prediction[0] == 1 else 'Benign'
    st.write(f'The prediction is: **{diagnosis}**')

    # Personalized suggestions
    if diagnosis == 'Malignant':
        st.write("""
        ### Personalized Suggestions For You:
        - **Please visit a healthcare professional immediately for further evaluation and diagnostic tests.**
        - Consider scheduling an appointment with a breast cancer specialist.
        - For more information, visit [local clinics or hospitals].
        """)
    else:
        st.write("""
        ### Personalized Suggestions For You:
        - **Continue regular self-examinations and routine check-ups.**
        - Maintain a healthy lifestyle and be vigilant about any changes.
        - Consider scheduling routine mammograms as recommended by your healthcare provider.
        """)

# Run this app in your local machine
# streamlit run app.py
