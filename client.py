import requests

# Define los datos de entrada para la predicción del tamaño de la ropa
body = {
    "weight": 60,
    "age": 33.0,
    "height": 180.64
}

# Realiza una solicitud POST a la URL de tu servicio FastAPI
response = requests.post(url='http://127.0.0.1:8000/predict', json=body)

# Imprime la respuesta que debería contener el tamaño de ropa predicho
print(response.json())
