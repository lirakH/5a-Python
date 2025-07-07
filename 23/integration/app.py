import streamlit as st
import requests
import pandas as pd

st.title('Project Management App')

# Developer Form
st.header("Add a Developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)

if st.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post("http://localhost:8000/developers/", json=dev_data)
    st.json(response.json())
