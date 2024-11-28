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

'''bash
Copy code
docker pull zaidtech/diabetes_model_prediction:latest

