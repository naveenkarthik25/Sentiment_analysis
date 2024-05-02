from fastapi import FastAPI
from transformers import pipeline
#Pydantic is a Python library for data parsing and validation.
# It uses thetype hinting mechanism of the newer versions of Python (version 3.6onwards) and
#validates the types during the runtime.
# Pydantic definesBaseModel class.
# #It acts as the base class for creating user defined models.
from pydantic import BaseModel
 
app = FastAPI()
#This app object is the main point of interaction of the application with the client browser.
 
class Janani(BaseModel):  #User defined models
    text: str
 
@app.post("/detail")
# Path is a URL which when visited by the client invokes visits a mapped URL to one of the HTTP methods,
# an associated function is to be executed.
# We need to bind a post function toa URL and the corresponding HTTP method.
def recall(request: Janani):  #function called recall
    pipe = pipeline("text-classification", model="syedkhalid076/RoBERTa-Sentimental-Analysis-Model")
    result = pipe(request.text)
    return result