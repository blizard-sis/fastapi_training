from fastapi import FastAPI

app = FastAPI()


@app.post(
    '/a',
    tags=['immutable'],
    summary='a',
    response_description='resp a'
)
def a() -> str:
    """
    descr a
    """
    return 'Вот это ответ!'


@app.get(
    '/b',
    tags=['mutable'],
    summary='b',
    description='descr b',
    response_description='resp b'
)
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']


@app.post(
    '/c',
    tags=['immutable'],
    summary='c',
    response_description='resp c'
)
def c() -> int:
    """
    descr c
    """
    return 42


@app.get(
    '/d',
    tags=['mutable'],
    summary='summary d',
    description='descr d',
    response_description='resp d'
)
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}
