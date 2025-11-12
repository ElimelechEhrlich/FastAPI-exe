from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from data import return_in_reversr, return_in_uppercase

app = FastAPI()   

class Item(BaseModel):
    text:str


item = Item()

@app.get("/reverse")
def get_reversr(q:str):
    return return_in_reversr(q)

@app.get("/uppercase/{text}")
def get_uppercase(text):
    t = {"name": text}
    return return_in_uppercase(t["name"])

@app.post("/remove-vowels")
def without_vowels_aeiou(item: Item):
    to_remove = 'aeiou'
    newitem:str = ''
    for singl in item.text:
        if singl not in to_remove: 
            newitem += singl
        return { "original": item.text, "without_vowels": newitem }







    






if __name__ == '__main__':
    uvicorn.run(app, '127.0.0.1', 8000)