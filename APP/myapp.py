# import libraries

import pandas as pd
import streamlit as st
import joblib

# set page layout
st.set_page_config(
    page_title='Crop Yield Prediction',
    layout='wide'
)

# function to load model
@st.cache_resource
def load_model(model_file_path):
    """
    Docstring for load_model
    
    param: model_file_path: provide file path of saved model
    returns: saved model
    """
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

# invokde function
crop_model = load_model(model_file_path=r'C:\Users\chill\programs\streamLIT\CropYieldprediction\Model\xgb_model.pkl')    
# title
st.title("Crop Yield Prediction App")

st.markdown("---")
# create two columns 
col_a, col_b = st.columns(2, gap='large', border=True, vertical_alignment='center')

# column 1 inputs
with col_a:
    # list of availble crops
    crop_options = [
        'Arecanut',
        'Arhar/Tur',
        'Castor seed',
        'Coconut',
        'Cotton(lint)',
        'Dry chillies',
        'Gram',
        'Jute',
        'Rice',
        'Linseed',
        'Maize',
        'Mesta',
        'Niger seed',
        'Wheat',
        'Onion',
        'Bajra',
        'Sugarcane',
        'Ginger',
        'Black pepper',
        'Khesari',
        'Banana',
        'Sweet potato',
        'Soyabean',
        'Masoor',
        'Potato',
        'Urad',
        'Groundnut',
        'Moong(Green Gram)',
        'Cashewnut',
        'Jowar']
    
    # list of Indian States
    state_options = [
        'Assam',
        'Andhra Pradesh',
        'Arunachal Pradesh',
        'Bihar',
        'Chhattisgarh',
        'Delhi',
        'Goa',
        'Haryana',
        'Himachal Pradesh',
        'Jharkhand',
        'Jammu and Kashmir',
        'Karnataka',
        'Kerala',
        'Meghalaya',
        'Madhya Pradesh',
        'Maharashtra',
        'Mizoram',
        'Manipur'
        'Nagaland',
        'Odisha',
        'Puducherry',
        'Punjab',
        'Sikkim',
        'Tamil Nadu',
        'Tripura',
        'Telangana',
        'Uttar Pradesh',
        'Uttarakhand',
        'West Bengal'
    ]
    crop = st.selectbox(label='Select Crop', options=crop_options, index=9)
    cropYear = st.number_input("select Year", min_value=1997, step=1)
    season = st.selectbox('Select season', ['Whole Year','Kharif','Autumn','Summer','Winter'])
    state = st.selectbox('Select state', options=state_options)
    area = st.number_input("Area", min_value=0, max_value=100000)

# column 2 inputs
with col_b:
    production = st.number_input("production", min_value=0)
    AnnualRainfall = st.number_input("Annual Rainfall (in mm)", min_value=0)
    fertilizer = st.number_input("Fertilizer amount", min_value=0)
    pesticide = st.number_input("presticide amount", min_value=0)

# create a dictionary of input data 
data = {
    'Crop': [crop],
    'Crop_Year': [cropYear],
    'Season': [season],
    'State': [state],
    'Area': [area],
    'Production': [production],
    'Annual_Rainfall': [AnnualRainfall],
    'Fertilizer': [fertilizer],
    'Pesticide': [pesticide]
}
# create dataframe
df = pd.DataFrame(data, index=[0])
# display review
st.subheader("Review")
st.table(data=df, border=True)
st.markdown('---')

# prediction button
if st.button('Predict', type='primary'):
    if crop_model is not None:
        with st.spinner('predicting...'):
            try:
                pred = crop_model.predict(df)
                if pred[0]:
                    st.success(f"Yield: {pred[0]:.2f}")
                else:
                    st.error("Prediction Failed.")
            except Exception as e:
                st.error(f"Error! {e}")