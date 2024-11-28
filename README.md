Diabetes Prediction API
Project Description
This project is a FastAPI-based web service that predicts the likelihood of diabetes in an individual based on various health-related input parameters. The machine learning model used in this project is trained on relevant medical data and is saved as a .sav file, which is loaded for predictions. The web service runs inside a Docker container and exposes a REST API for easy interaction.

Pull the Docker Image 📥
You can pull the latest Docker image of the project from Docker Hub:

'''bash
Copy code
docker pull zaidtech/diabetes_model_prediction:latest
Run the Docker Container 🏃‍♂️
After pulling the image, you can run the container with the following command:

bash
Copy code
docker run -d -p 8000:8000 zaidtech/diabetes_model_prediction:latest
This will start the container in detached mode and expose the API on port 8000 of your local machine.

Test the Diabetes Prediction API 🌐
Once the container is up and running, you can test the diabetes prediction API by sending a POST request with input data to:

bash
Copy code
http://localhost:8000/diabetes_prediction
The input should include health parameters such as pregnancies, glucose levels, blood pressure, BMI, age, and others. The API will return whether the person is diabetic or not based on the prediction model.

Docker Image Information 🐳
Image Name: zaidtech/diabetes_model_prediction
Tag: latest
Docker Hub URL: Docker Hub Repository
