# Diabetes Prediction Model

This project is a **Diabetes Prediction Model** developed using **FastAPI** and a **Machine Learning** model to predict whether a person has diabetes or not based on various health parameters.

## Project Overview
This project uses a pre-trained machine learning model that takes several health indicators (such as age, BMI, blood pressure, glucose levels, etc.) and predicts if a person is diabetic. The application is built using **FastAPI** and is containerized using **Docker**.

## Technologies Used:
- Python
- FastAPI
- Scikit-learn (for machine learning)
- Docker
- Uvicorn (ASGI server)
- Pydantic (for data validation)

## Prerequisites

- Python 3.11+
- Docker
- Git

### Install the required libraries:

```bash
pip install -r requirements.txt
Pull the Docker Image 📥
You can pull the latest Docker image of the project from Docker Hub:

bash
Copy code
docker pull zaidtech/diabetes_model_prediction:latest
Run the Docker Container 🏃‍♂️
After pulling the image, you can run the container with the following command:

bash
Copy code
docker run -d -p 8000:8000 zaidtech/diabetes_model_prediction:latest
Test the Diabetes Prediction API 🌐
Once the container is up and running, you can test the diabetes prediction API by sending a POST request to:

text
Copy code
http://localhost:8000/diabetes_prediction
The API accepts the following JSON body for prediction:

json
Copy code
{
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 25,
    "Insulin": 0,
    "BMI": 32.2,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 45
}
Example Request:
Use a tool like Postman or curl to send the POST request.

bash
Copy code
curl -X 'POST' \
  'http://localhost:8000/diabetes_prediction' \
  -H 'Content-Type: application/json' \
  -d '{
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 25,
    "Insulin": 0,
    "BMI": 32.2,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 45
}'
Docker Image Information 🐳
Image Name: zaidtech/diabetes_model_prediction
Tag: latest
Docker Hub URL: Docker Hub Repository
