from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def multiplication(
        length: int,
        width: int,
        depth: Optional[int] = None,
) -> dict[int]:
    result = length * width
    if depth is not None:
        result *= depth
    return result
