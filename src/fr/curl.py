import requests

def get_weight(l, url="http:localhost:8001/fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    weight = j.get("weight")
    return weight

def get_knn(url="http://localhost:8002/fish"):
    length = input("🐋물고기의 길이를 입력하세요")
    headers = {
        'accept': 'application/json',
    }
    w = get_weight(length)
    params = {
        'length': length,
        'weight' : w,
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    fish_name = j.get("prediction")
    print(f"길이 : {length}, 예측된 무게 : {w}, 예측된 물고기 : {fish_name}")
    return fish_name
