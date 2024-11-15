import json
import requests
url='http://127.0.0.1:8000/diabetes_prediction'
test_data={
    
        'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
}
input_json=json.dumps(test_data)
response = requests.post(url, data=input_json)
if response.status_code==200:
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}") 
