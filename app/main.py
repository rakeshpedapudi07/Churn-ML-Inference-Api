import os
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "churn_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

class CustomerInput(BaseModel):
    credit_score: int
    age: int
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float
    country_Germany: int
    country_Spain: int
    gender_Male: int

@app.post("/predict")
def predict(data: CustomerInput):
    X = pd.DataFrame([data.model_dump()])
    prediction = model.predict(X)[0]
    return {"churn_prediction": int(prediction)}
