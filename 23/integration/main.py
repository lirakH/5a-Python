from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")
def create_developer(developer: Developer):
  return {"message": "Developer creadet successfuly", "developer": developer}

@app.post("/projects/")
def create_project(project: Project):
  return {"message": "Project creadet successfuly", "project": project}

@app.get("/projects/")
def get_projects():
  #This is placeholder; in a real application, you'd fetch this data from a database
  sample_project = Project(
    title = "Sample",
    description = "This is a sample project",
    languages = ["Python" "JavaScript", "HTML"],
    lead_deeloper = Developer(name="John Doe", experience=5)
  )
  return {"projects": [sample_project]}
