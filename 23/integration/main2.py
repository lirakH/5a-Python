from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from models import Developer, Project

app = FastAPI()

# Sample project
sample_project = Project(
    title="Sample Project",
    description="This is a sample project",
    languages=["Python", "JavaScript"],
    lead_developer=Developer(name="Jane Doe", experience=5)
)

# In-memory lists with sample project already included
developers = [sample_project.lead_developer]
projects = [sample_project]

@app.post("/developers/")
def create_developer(developer: Developer):
    developers.append(developer)
    return {"message": "Developer created successfully", "developer": developer}

@app.get("/developers/")
def get_developers():
    return {"developers": jsonable_encoder(developers)}

@app.post("/projects/")
def create_project(project: Project):
    projects.append(project)

    # Optionally add lead developer to developer list (if not already)
    if not any(dev.name == project.lead_developer.name and dev.experience == project.lead_developer.experience for dev in developers):
        developers.append(project.lead_developer)

    return {"message": "Project created successfully", "project": project}

@app.get("/projects/")
def get_projects():
    return {"projects": jsonable_encoder(projects)}
