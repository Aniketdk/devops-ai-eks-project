# AI App Deployment on AWS EKS with GitHub Actions CI/CD

## Overview

This project demonstrates a complete **DevOps pipeline** for deploying a Python AI app using:

- **Docker** – containerization  
- **AWS EKS** – managed Kubernetes cluster  
- **GitHub Actions** – CI/CD workflow  
- **DockerHub** – container registry  

Every push to the `main` branch triggers the pipeline to:

1. Build the Docker image  
2. Push the image to DockerHub  
3. Deploy the app to the EKS cluster  
4. Automatically update the Kubernetes deployment  

---

## Project Structure

- `app.py` – Flask AI application  
- `requirements.txt` – Python dependencies  
- `Dockerfile` – Docker container configuration  
- `k8s/` – Kubernetes manifests for deployment and service  
- `.github/workflows/` – CI/CD pipeline workflow  

---

## GitHub Actions CI/CD

The workflow performs:

- Checkout of code from GitHub  
- AWS authentication and kubeconfig setup  
- DockerHub login  
- Docker image build & push  
- Kubernetes deployment update  

---

## Environment Variables / Secrets

Set the following GitHub secrets for CI/CD:

- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `DOCKER_USERNAME`  
- `DOCKER_PASSWORD`  

---

## Local Testing

- Configure kubeconfig to connect to EKS:  

aws eks update-kubeconfig --region ap-south-1 --name ai-eks-cluster
kubectl get nodes

## Build and run Docker image locally:

docker build -t aniketdk/ai-app:latest .
docker run -p 5000:5000 aniketdk/ai-app:latest

- Deploy manually to EKS if needed

- Monitor deployments and pods using kubectl

## Tech Stack

- Python 3.x + Flask

- Docker

- Kubernetes (EKS)

- GitHub Actions

- AWS CLI / eksctl

- DockerHub

## Notes

- Rolling updates ensure old pods are replaced automatically

- EKS cluster is managed and scalable

- Application is exposed externally via LoadBalancer

- Live Demo
http://a06d4b8f5d69640e3868a20ca0d21627-1871388415.ap-south-1.elb.amazonaws.com/
