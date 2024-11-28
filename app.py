from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()


class InputData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


model_prediction = pickle.load(open('diabetes_model.sav', 'rb'))


@app.get('/')
def root():
    return {'message': 'Welcome to the Diabetes Prediction API'}


@app.get('/{name}')
def get_name(name: str):
    return {'Hello Dear': name}


@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters: InputData):
    input_dictionary = input_parameters.dict()
    list_input = [
        input_dictionary['Pregnancies'],
        input_dictionary['Glucose'],
        input_dictionary['BloodPressure'],
        input_dictionary['SkinThickness'],
        input_dictionary['Insulin'],
        input_dictionary['BMI'],
        input_dictionary['DiabetesPedigreeFunction'],
        input_dictionary['Age']
    ]

    prediction = model_prediction.predict([list_input])
    if prediction[0] == 0:
        result = 'The person is not diabetic'
    else:
        result = 'The person is diabetic'

    return {'prediction': result}
