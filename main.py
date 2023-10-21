from typing import Optional
from enum import Enum

from fastapi import FastAPI, Path, Query

app = FastAPI()


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me')
def hello_author() -> dict[str, str]:
    return {'Hello': 'author'}


@app.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия'
)
def greetings(
        *,
        name: str = Path(
            ..., min_length=2, max_length=20,
            title='Полное имя', description='Можно вводить в любом регистре'
        ),
        surname: str = Query(..., min_length=2, max_length=50),
        age: Optional[int] = Query(None, gt=4, le=99),
        is_staff: bool = Query(False, alias='is-staff'),
        education_level: Optional[EducationLevel] = None, 
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
