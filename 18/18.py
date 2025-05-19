"""
Displaying and Visualizing Data in Streamlit 


st.write("fjali")

st.write(array)

"""

import streamlit as st
import pandas as pd


data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [14, 16, 15],
    "City": ["Ferizaj", "Prishtina", "Peja"]
})


st.write(data)


"""
[] - array 1 dimensionale
[()] - array 2 dimensionale
[({})] - array 3 dimensionale

[()()()] - array 2 dimensionale

"""






