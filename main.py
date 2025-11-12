from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from data import read_in_reversr

app = FastAPI()    

@app.get("/reverse")
def get_reversr(q:str):
    return read_in_reversr(q)



    






if __name__ == '__main__':
    uvicorn.run(app, '127.0.0.1', 8000)