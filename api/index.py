from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data from q-vercel-python.json
file_path = os.path.join(os.path.dirname(__file__), "../q-vercel-python.json")
with open(file_path, "r") as file:
    data = json.load(file)

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    marks = [item["marks"] for item in data if item["name"] in name]
    return {"marks": marks}