
● Streamlit will be used for the frontend, providing a user interface for managing developers and projects. 
● FastAPI will handle the backend, managing the logic for handling API requests. 
● Pydantic will be used to define and validate the data models. 

● app.py: This will contain the Streamlit code for the user interface. 
● main.py: This will contain the FastAPI backend code. 
● models.py: This will contain the Pydantic models for data validation. 

We begin by defining the data models using Pydantic, which will ensure that the data we receive is correctly formatted and validated before any processing. 
● Developer model: This model has two attributes: name (a required string) and experience (an optional integer). 
● Project model: This model includes attributes for the project's title, description, languages used (a list of strings), and a lead developer (which is itself a Developer model). 

Next, we will implement the FastAPI backend, which will handle incoming POST requests for creating developers and projects. 
● create_developer: This endpoint takes a Developer object as input and returns a success message along with the developer data. 
● create_project: This endpoint takes a Project object as input and returns a success message along with the project data. 
● get_projects: This is an additional GET endpoint that returns a list of projects. Here, we've added a sample project for demonstration purposes, but in a real application, you would fetch the project data from a database. 

Finally, we create the user interface with Streamlit. This will include forms for users to input developer and project information, as well as a dashboard to display the projects: 
● Developer Form: The user inputs a developer's name and experience. When the button is clicked, this data is sent to the FastAPI backend, and the response (including the developer data) is displayed. 
● Project Form: The user inputs the project's title, description, languages used, and lead developer details. On clicking the button, this data is sent to the FastAPI backend, and the response is displayed. 
● Display Projects in Dashboard: This section fetches and displays existing projects when the "Get Projects" button is clicked (in our case the sample_project). 
● Projects Overview Table: A table displaying all the projects fetched from the backend. 
● Project Details: Each project's details are shown in a structured format using Markdown, making it easy to read and understand the project's specifics. 


To run the application, make sure: 
● Start the FastAPI server: uvicorn main:app --reload 
● Run the Streamlit app: streamlit run app.py 

ose 

(v2)
● Start the FastAPI server: uvicorn main2:app --reload 
● Run the Streamlit app: streamlit run app.py 

Tek verzioni 2 e kam shtu nje memorie te perkohshme ne vend te databazes qe nuk e kemi akoma
Tash mundemi me shtu projekte edhe kur i themi paraqiti projektet duhet me u paraqite edhe projekti qe e shtojme
