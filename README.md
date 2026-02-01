🚨 End-to-End MLOps Pipeline for Network Security Threat Detection
📌 Overview

This repository demonstrates a production-grade Machine Learning Operations (MLOps) pipeline applied to cybersecurity—specifically for detecting malicious activities such as:

Phishing URLs

Intrusion attempts

Suspicious network traffic

The project integrates the complete ML lifecycle:

Data Engineering

Model Development

Experiment Tracking

CI/CD Automation

Containerization

Cloud Deployment

The result is a scalable, reproducible, and automated system suitable for real-world enterprise security operations.

🎯 Problem Statement

The objective is to automatically classify network activity—such as URLs or packets—as safe or malicious using machine learning.

Beyond model accuracy, this project focuses heavily on:

Pipeline automation

Model versioning

Continuous retraining

Production deployment

Monitoring & reproducibility

✨ Key Features
🔄 Automated Data Ingestion

Pulls network traffic or URL-based datasets from configurable sources.

🧠 ML Pipelines

End-to-end orchestration covering:

Data validation

Feature engineering

Model training

Model evaluation

📊 Experiment Tracking

Logs metrics, parameters, and artifacts using:

MLflow

DagsHub / DVC

🚀 CI/CD Integration

Automated testing & deployment using GitHub Actions.

🐳 Containerization

Dockerized services for consistent execution across environments.

🌐 Model Deployment

REST API inference service built using FastAPI.

Cloud-ready for AWS / Azure.

🛠️ Technologies Used
🔹 Machine Learning

Scikit-learn

TensorFlow / PyTorch

🔹 MLOps & Tracking

MLflow

DVC / DagsHub

🔹 Orchestration

Prefect / Apache Airflow

🔹 CI/CD

GitHub Actions

🔹 Deployment

Docker

FastAPI

AWS / Azure

📊 Project Outcome

This system enables:

✅ Continuous data ingestion
✅ Automatic retraining
✅ Model version tracking
✅ CI/CD-driven deployments
✅ Real-time prediction APIs

The architecture mirrors enterprise-grade ML platforms used in security operations centers (SOC).

⚙️ Setup & Installation
🔹 Clone Repository

git clone <repository_url>
cd network-security-mlops


🔹 Create Virtual Environment

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


🔹 Install Dependencies

pip install -r requirements.txt

🔹 Run Pipelines Locally

python main.py

🔹 Start API Service

uvicorn api.main:app --reload

📁 Project Structure

├── data/
├── pipelines/
├── components/
├── config/
├── models/
├── notebooks/
├── api/
├── Dockerfile
├── .github/workflows/
├── requirements.txt
└── README.md

🛡️ Network Security – Phishing Detection

🔐 GitHub Secrets Setup

Configure the following secrets inside your GitHub repository:

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-east-1

AWS_ECR_LOGIN_URI=788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity
ECR_REPOSITORY_NAME=networkssecurity

🐳 Docker Setup on EC2

🔹 Update System (Optional)

sudo apt-get update -y
sudo apt-get upgrade -y

🔹 Install Docker (Required)

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

🔹 Add User to Docker Group

sudo usermod -aG docker ubuntu
newgrp docker

🔹 Verify Installation

docker --version

🚀 Future Enhancements (Optional)

Monitoring with Prometheus & Grafana

Canary deployments

Model drift detection

Feature store integration

Automated rollback strategies

Kubernetes orchestration

