from typing import Union
from fastapi import FastAPI
import pickle
from fr.lr import lr_api 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float):
    """
    물고기의 무게 예측기

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        dict: 물고기 무게를 담은 딕셔너리
    """
    weight = lr_api(length)

    return {
                "length": length, 
                "weight": weight
            }
