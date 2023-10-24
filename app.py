from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/math-sum')
def default(
        add: list[float] = Query(..., gt=0, lt=10),
) -> float:
    result = 0
    for ad in add:
        result += ad
    return result
