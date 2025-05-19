import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

# Streamlit app title and description
st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022.")

# Summary Statistics
st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

# Display summary statistics in a row of metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

