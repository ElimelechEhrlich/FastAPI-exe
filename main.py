from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from string_ops import reverse_str, to_upper, remove_vowels, remove_every_third, letter_counts_map

app = FastAPI()   

class Item(BaseModel):
    text:str

@app.get("/reverse")
def get_reversr(q:str):
    return reverse_str(q)

@app.get("/uppercase/{text}")
def get_uppercase(text):
    t = {"name": text}
    return to_upper(t["name"])

@app.post("/remove-vowels")
def post_remove_vowels(item:Item):
    return remove_vowels(item.text)
    
@app.post("/remove_every_third")
def post_remove_third(item:Item):
    return remove_every_third(item.text)

@app.post("/letter-counts")
def post_letter_counts(item:Item):
    return letter_counts_map(item.text)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost' ,port=8000)