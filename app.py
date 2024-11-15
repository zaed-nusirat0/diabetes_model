from fastapi import FastAPI
import pickle
import json
from pydantic import BaseModel
import uvicorn 
import requests

app=FastAPI()

class input_data(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    
model_prediction=pickle.load(open('diabetes_model.sav','rb'))
@app.get('/')

def root():
    return {'hello':'name'}

@app.get('/{name}')

@app.get('/{name}')
def get_name(name:str):
  return {'Hello Dear : ': f'{name}'}

@app.post('/diabetes_prediction')

def diabetes_predd(input_parameters:input_data):
    input_dictionary =input_parameters.dict()
    
    preg = input_dictionary['Pregnancies']
    
    glu = input_dictionary['Glucose']
    
    bp = input_dictionary['BloodPressure']
    
    skin = input_dictionary['SkinThickness']
    
    insulin = input_dictionary['Insulin']
    
    bmi = input_dictionary['BMI']
    
    dpf = input_dictionary['DiabetesPedigreeFunction']
    
    age = input_dictionary['Age']
    
    list_input=[preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction=model_prediction.predict([list_input])
    if prediction[0]==0:
        result = 'The person is not diabetic'
    else:
        result = 'The person is diabetic'
        
    return {'prediction':result}
        

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

