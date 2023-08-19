# Text Summarizer 

This project is a text summarizer that utilizes the Pegasus Model for automatic text summarization.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technology Used](#technology-used)
- [Installation](#installation)
- [AWS CICD Deployment with Github Actions](#aws-cicd-deployment-with-github-actions)
- [Preview of Text Summarizer in Action](#preview-of-text-summarizer-in-action)
- [License](#license)

## Introduction

The Text Summarizer Project aims to automatically generate concise and coherent summaries of given text inputs. Summarization is accomplished through the utilization of the Pegasus model (PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization), which employs an  approach to extract the most important sentences from the input text.

## Features
- **Automatic Summarization:** Generate summaries from given text inputs.
- **Pegasus Model:** Utilize the advanced Pegasus Model for summarization.
- **Concise Output:** Receive concise and coherent summaries of text content.

## Technology Used

This project leverages various technologies to achieve its goals:

- **Programming Language:** Python
- **HuggingFace:** The Pegasus Model, a state-of-the-art model for text summarization.
- **FastAPI:** A modern, fast web framework for building APIs with Python.
- **Docker:** A platform to develop, ship, and run applications in containers.
- **Amazon Web Services (AWS):** A cloud computing platform that provides various services and tools to facilitate deployment and management of applications.
  - **AWS Identity and Access Management (IAM):** Used to manage access to AWS resources securely.
  - **Elastic Container Registry (ECR):** A managed container registry to store, manage, and deploy Docker container images.
  - **Amazon Elastic Compute Cloud (Amazon EC2):** Provides scalable compute capacity in the cloud, often used to host applications and services.

These technologies come together to create an automated text summarization solution that utilizes the power of AI models, web frameworks, containers, and cloud services to generate concise and coherent summaries from text inputs.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/SahilChowkekar/Text-Summarizer.git

```

2. Navigate to the project directory:
```bash
cd Text-Summarizer

```
3. Create a conda environment after opening the repository:
```bash
conda create -n textsummary python=3.8 -y
```

4. Activate the conda environment:
```bash
conda activate textsummary
```
5. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Finally, run the following command to start the application:
```bash
python app.py
```

7. Open your preferred web browser and visit:
```bash
http://localhost:8080

```












# AWS CICD Deployment with Github Actions

This repository provides instructions and steps to deploy an application using AWS services and GitHub Actions for continuous integration and continuous deployment (CI/CD).

## 1. Login to AWS console

Login to your AWS console using your credentials.

## 2. Create IAM user for deployment

Create an IAM user with specific access for deployment purposes, including EC2 and ECR access. Attach the following policies:

- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2FullAccess

## 3. Create ECR repo to store/save Docker image

Create an Elastic Container Registry (ECR) repository to store your Docker image. Save the repository URI, e.g., `062582090401.dkr.ecr.us-east-2.amazonaws.com/text-s`.

## 4. Create EC2 machine (Ubuntu)

Create an EC2 instance with the Ubuntu operating system.

## 5. Install Docker in EC2 Machine

Connect to your EC2 instance and install Docker:

```bash
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

## 6. Configure EC2 as self-hosted runner
Go to your repository settings in GitHub, navigate to Actions, and set up a new self-hosted runner. Choose the appropriate OS and follow the provided commands

## 7. Setup GitHub secrets
In your GitHub repository, go to Settings > Secrets and add the following secrets:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
- `AWS_REGION`: The AWS region you are using (e.g., `us-east-2`).
- `AWS_ECR_LOGIN_URI`: The ECR login URI (e.g., `062582090401.dkr.ecr.us-east-2.amazonaws.com/text-s`).
- `ECR_REPOSITORY_NAME`: The name of your ECR repository (e.g., `textsummary-app`).

Now, your GitHub Actions workflows can securely access the required AWS resources using these secrets.


Feel free to follow these steps to set up a seamless CI/CD pipeline for deploying your application using AWS services and GitHub Actions.


Please make sure to review and adjust the content as needed, especially the specific AWS resource names and regions based on your project.

## Preview of Text Summarizer in Action

Here's a preview of the Text Summarizer application in action:

![Text Summarizer Screenshot](images/text-summarizer-screenshot.png)

![Text Summarizer Screenshot](images/text-summarizer-screenshot.png)



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.