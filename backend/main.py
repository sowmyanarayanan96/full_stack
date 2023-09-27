from typing import List


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class person(BaseModel):
    id:int
    name:str
    age:int


db : List[person] = [
    person(id=1, name="nithin", age=26),
    person(id=2, name="sowmy", age=27),
    person(id=3, name="sai", age=27),
    person(id=4, name="priya", age=24)
]


@app.get("/api")
def read_root():
    return db


