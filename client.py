import requests

body = {
    "weight": 65,
    "age": 33.0,
    "height": 165.64
}

response = requests.post(url='http://127.0.0.1:8000/predict', json=body)

print(response.json())
