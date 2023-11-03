from pydantic import BaseModel
from joblib import load
import numpy as np
from fastapi import FastAPI


app = FastAPI(title='Clothing Size Prediction')

class InputData(BaseModel):
    weight: float
    age: float
    height: float

class OutputData(BaseModel):
    size: str


model = load('./model/ropa-size-prediction.joblib')
label_encoder = load('model/label_encoder.joblib')

@app.post('/predict', response_model=OutputData)
def predict(data: InputData):

    weight = data.weight
    age = data.age
    height = data.height

   
    model_input = np.array([[weight, age, height]])
    prediction = model.predict(model_input)
    predicted_size = label_encoder.inverse_transform([int(round(prediction[0]))])[0]

    return {'size': predicted_size}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
