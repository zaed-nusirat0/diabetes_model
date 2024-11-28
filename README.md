# Diabetes Prediction Model

This project is a **Diabetes Prediction Model** built using **FastAPI** and a **Machine Learning** model. It predicts whether a person is diabetic or not based on health-related parameters like age, BMI, glucose levels, etc. The project is containerized using **Docker** for easy deployment.

## Features ✨

- **Dockerized model** for easy deployment 🚀
- **Predicts diabetes risk** based on health parameters 🏥
- **API endpoint** for making predictions 🔮
- Exposes port 8000 (can be configured) 🌍
- Supports both local and cloud deployments ☁️

## How to Use ⚙️

Follow these steps to get the application running on your local machine:

### Prerequisites ⚠️

1. **Docker** must be installed on your system. You can install Docker by following the official installation guide here:  
   [Docker Installation](https://docs.docker.com/get-docker/)

### Pull the Docker Image 📥

You can pull the latest Docker image of the project from Docker Hub:

```bash
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
You can use a tool like Postman or curl to send the POST request:

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
