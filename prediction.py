import streamlit as st
import pandas as pd
import pickle
import joblib

from sklearn.ensemble import RandomForestClassifier
import base64

# Save the model
model = joblib.load('drug_prediction_rf.pkl')
joblib.dump(model, 'drug_prediction_rf.pkl')

# Define the input features
features = ['age', 'gender', 'season', 'prognosis']

# # Define a dictionary to store the input values
# input_data = {}

# Create the Streamlit app
st.set_page_config(page_title="Medical Condition Prediction", page_icon=":clipboard:")

st.title("Drug Prediction")

# Initialize the input data with all zeros
input_data = {'age': 0,
              'gender_M': 0,
              'season_MONSOON ': 0,
              'season_SPRING':0,
              'season_SUMMER':0,
              'season_WINTER':0,
              'prognosis_AIDS': 0,
              'prognosis_Acne': 0,
              'prognosis_Alcoholic hepatitis': 0,
              'prognosis_Allergy': 0,
              'prognosis_Arthritis': 0,
              'prognosis_Bronchial Asthma': 0,
              'prognosis_Cervical spondylosis': 0,
              'prognosis_Chicken pox': 0,
              'prognosis_Chronic cholestasis': 0,
              'prognosis_Common Cold': 0,
              'prognosis_Dengue': 0,
              'prognosis_Jaundice': 0,
              'prognosis_Malaria': 0,
              'prognosis_Migraine': 0,
              'prognosis_Osteoarthristis': 0,
              'prognosis_Peptic ulcer diseae': 0,
              'prognosis_Pneumonia': 0,
              'prognosis_Psoriasis': 0,
              'prognosis_Tuberculosis': 0,
              'prognosis_Typhoid': 0,
              'prognosis_Urinary tract infection': 0,
              'prognosis_Varicose veins': 0}

# Collect the input values from the user
input_data["age"] = st.slider("Age", min_value=15, max_value=100, value=50)

# Collect gender information
st.subheader("Gender")
gender_options = ['M', 'F']
gender = st.radio("Select gender", gender_options)
if gender == 'M':
    input_data[f'gender_{gender}'] = 1
else:
    input_data[f'gender_M'] = 0

# Collect season information
st.subheader("Season")
season_options = ['MONSOON ', 'SPRING', 'SUMMER', 'WINTER']
season = st.radio("Select season", season_options)
input_data[f'season_{season}'] = 1

# Collect prognosis information
st.subheader("Prognosis")
prognosis_options = ['AIDS', 'Acne', 'Alcoholic hepatitis', 'Allergy', 'Arthritis', 
                     'Bronchial Asthma', 'Cervical spondylosis', 'Chicken pox', 
                     'Chronic cholestasis', 'Common Cold', 'Dengue', 'Jaundice', 
                     'Malaria', 'Migraine', 'Osteoarthristis', 'Peptic ulcer diseae', 
                     'Pneumonia', 'Psoriasis', 'Tuberculosis', 'Typhoid', 
                     'Urinary tract infection', 'Varicose veins']
prognosis = st.radio("Select prognosis", prognosis_options)
input_data[f'prognosis_{prognosis}'] = 1

# Convert the input data into a DataFrame
input_df = pd.DataFrame([input_data])

# Get the model predictions
predictions = model.predict(input_df)
predict = label_encoder.inverse_transform(predictions)

# # Display the predictions
# st.button('prediction',key='predict')
# if st.session_state.get("predict"):
#     # file()  
#     st.subheader("Predictions")
#     st.write('Drug', ":", predict[0])


# Get the model predictions
predictions = model.predict(input_df)
predict = label_encoder.inverse_transform(predictions)

# Display the predictions
st.button('prediction',key='predict')
if st.session_state.get("predict"):
    # file()  
    st.subheader("Predictions")
    st.write('Drug', ":", predict[0])

#defining function to set background of app
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background(r"drugs.jpg")