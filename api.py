from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()

def read_data():
    

@app.get
def get_items():
    return 