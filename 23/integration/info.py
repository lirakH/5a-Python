"""
● Streamlit will be used for the frontend, providing a user interface for managing developers and projects. 
● FastAPI will handle the backend, managing the logic for handling API requests. 
● Pydantic will be used to define and validate the data models. 

● app.py: This will contain the Streamlit code for the user interface. 
● main.py: This will contain the FastAPI backend code. 
● models.py: This will contain the Pydantic models for data validation. 

We begin by defining the data models using Pydantic, which will ensure that the data we receive is correctly formatted and validated before any processing. 
● Developer model: This model has two attributes: name (a required string) and experience (an optional integer). 
● Project model: This model includes attributes for the project's title, description, languages used (a list of strings), and a lead developer (which is itself a Developer model). 

"""
