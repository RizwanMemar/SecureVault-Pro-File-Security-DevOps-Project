# 🔐 SecureVault Pro – File Security & DevOps Project

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI](https://img.shields.io/badge/GitHub%20Actions-CI%20Passing-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 🚀 Project Overview

SecureVault Pro is a Flask-based cybersecurity web application that analyzes uploaded files for:

- MD5, SHA1, SHA256 hashing
- File type detection
- Risk scoring engine
- Basic malware detection (hash-based)
- Image to PDF conversion
- OCR (Image to Text simulation / optional real OCR support)

It is built as a DevOps-integrated project demonstrating the full workflow from development to deployment.

---

## 🧰 Features

- 🔐 File hash generation (MD5, SHA1, SHA256)
- ⚠️ Risk analysis engine
- 🛡 Malware detection (signature-based)
- 🖼 Image → PDF converter
- 🔍 Image → Text (OCR)
- 🧰 Tools dashboard (multi-page UI)
- 💻 Hacker-style terminal animation UI
- 🌐 Flask web interface

---

## ⚙️ Technologies Used

- Python (Flask)
- HTML / CSS / JavaScript
- Docker
- Git & GitHub
- GitHub Actions (CI Pipeline)
- Terraform (Infrastructure simulation)
- ReportLab (PDF generation)

---

## 🧱 Architecture Diagram

                    ┌────────────────────┐
                    │     User Browser   │
                    └─────────┬──────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Flask Web Application  │
                │   (SecureVault Pro)      │
                └─────────┬────────────────┘
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
┌──────────────┐  ┌────────────────┐  ┌──────────────────┐
│ File Upload  │  │ Security Engine │  │ Tools Module     │
│              │  │                │  │                  │
│ - Upload     │  │ - MD5 / SHA    │  │ - Image→PDF      │
│ - Store file │  │ - Risk Score   │  │ - OCR (Text)     │
└──────────────┘  │ - Malware Check │  │ - TXT→PDF        │
                  └───────┬────────┘  └─────────┬────────┘
                          │                      │
                          ▼                      ▼
                ┌────────────────────────────────────┐
                │        Processing Layer            │
                │  - Hash Generator (SHA/MD5/SHA256)│
                │  - Risk Analysis Engine           │
                └──────────────────┬────────────────┘
                                   ▼
                    ┌────────────────────────┐
                    │   Docker Container     │
                    │ (Portable Deployment)  │
                    └─────────┬──────────────┘
                              ▼
                    ┌────────────────────────┐
                    │ GitHub Actions (CI/CD) │
                    │ - Build & Test         │
                    │ - Docker validation    │
                    └─────────┬──────────────┘
                              ▼
                    ┌────────────────────────┐
                    │ Terraform (IaC Layer)  │
                    │ - Infrastructure setup │
                    └────────────────────────┘

---

## ⚙️ Full Setup & Dependencies

1. Clone Repository
-------------------

git clone https://github.com/your-username/securevault-pro.git
cd securevault-pro


2. Create Virtual Environment
-----------------------------

python -m venv venv


3. Activate Virtual Environment
-------------------------------

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate


4. Install Dependencies
-----------------------

pip install -r requirements.txt


5. Install OCR Engine (IMPORTANT)
---------------------------------

This project uses Tesseract OCR for Image → Text functionality.

Download Tesseract OCR:
https://github.com/UB-Mannheim/tesseract/wiki

Add this path to Windows Environment Variables:

C:\Program Files\Tesseract-OCR


6. Run Flask Application
------------------------

python app.py


Open in browser:
http://127.0.0.1:5000


---

## 🐳 Docker Setup

Build Docker image:

docker build -t securevault .


Run Docker container:

docker run -p 5000:5000 securevault


---

## ☁️ Terraform Setup

cd terraform

terraform init

terraform apply


---

## 🔄 CI/CD Pipeline

GitHub Actions automatically performs:

- Code checkout
- Python setup
- Dependency installation
- Application syntax testing
- Docker image build validation

Workflow file:
.github/workflows/ci.yml


---

## 📁 Project Structure

app.py
templates/
static/
uploads/
Dockerfile
requirements.txt
README.md
terraform/
.github/workflows/


---

## 🎯 DevOps Concepts Demonstrated

- Application Development
- Version Control with Git
- Containerization using Docker
- Continuous Integration (CI/CD)
- Infrastructure as Code (Terraform)
- Local deployment workflow


---

## 👨‍💻 Author

Qaisar Rizwan Memar  
Student at the American University of Afghanistan