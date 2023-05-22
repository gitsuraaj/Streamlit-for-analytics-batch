import streamlit as st
import pandas as pd
import pickle


st.title("Car Predictions Application")

col1, col2= st.columns(2)

with col1:
    fuel_type= st.radio(
    "Select Fuel Type",
    ('Diesel', 'Petrol', 'CNG', 'LPG', "Electric"))

with col2:
    transmission= st.selectbox("Select Transmission Type",
    ('Manual', 'Automatic'))



col1, col2= st.columns(2)

with col1:
    engine= st.slider(
    'Select the engine power',
    500,5000, step=100)

with col2:
    seats= st.selectbox("Select Number of Seats", [4,5,6,7,8])



encode_dict= {"fuel_type": {"Diesel": 1, "Petrol": 2, "CNG":3, "LPG":4, "Electric": 5},
              "transmission": {"Manual": 1, "Automatic": 2 }

              }


def model_pred (fuel_type, transmission, engine, seats):
    with open ("car_pred", "rb") as file:
        reg_model= pickle.load(file)

    x_test=[[ 2018.0, 1, 40000,fuel_type,transmission, 18.00, engine, 85, seats ]]
    return reg_model.predict(x_test)


if st.button('Predict'):
    fuel_type= encode_dict['fuel_type'][fuel_type]
    transmission = encode_dict['transmission'][transmission]

    price=model_pred (fuel_type,transmission, engine, seats)

    st.write(f"Predicted Price is {price} ")

else:
    st.write('Hit the Predict Button')