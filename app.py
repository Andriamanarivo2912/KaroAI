from fastapi import FastAPI
from pydantic import BaseModel
from src.financial_researcher.crew import run_crew  # j’utilise ta logique

app = FastAPI()

class Query(BaseModel):
    input: str

@app.get("/")
def root():
    return {"message": "🚀 Financial Researcher (CrewAI) est en ligne sur Render"}

@app.post("/run")
def run_agent(query: Query):
    result = run_crew(query.input)
    return {"result": result}
