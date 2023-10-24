from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]


class Person(BaseModel):
    name: str
    surname: str


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    result = ' '.join([person.name, person.surname])
    result = result.title()
    return {'Hello': result}
