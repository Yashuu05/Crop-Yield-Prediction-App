# import libraries

import pandas as pd
import streamlit as st
import joblib


# set page layout
st.set_page_config(
    page_title='Crop Yield Prediction',
    layout='wide',
    initial_sidebar_state='expanded'
)

# create sidebar
st.sidebar.header("Attribute Information")


# function to load model
@st.cache_resource
def load_model(model_file_path):
    try:
        with st.spinner("waking up model..."):
            model = joblib.load(model_file_path)
            st.success("Model Loaded Successfully!")
            return model
    except FileNotFoundError:
        st.error("Error! model file not found.")
        return None
    except Exception as e:
        st.error(f"Error! {e}")
        return None

# provide file path of model
# invokde function
crop_model = load_model(model_file_path=r'C:\Users\chill\programs\streamLIT\CropYieldprediction\Model\xgb_model.pkl')    