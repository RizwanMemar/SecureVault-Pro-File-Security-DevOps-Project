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

## 🧱 Architecture Diagram

```text
                    ┌────────────────────┐
                    │    User Browser    │
                    └─────────┬──────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │  Flask Web Application   │
                │    (SecureVault Pro)     │
                └─────────┬────────────────┘
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼

┌──────────────┐  ┌────────────────┐  ┌──────────────────┐
│ File Upload  │  │ Security Engine│  │   Tools Module   │
│              │  │                │  │                  │
│ - Upload     │  │ - MD5 / SHA    │  │ - Image → PDF    │
│ - Store File │  │ - Risk Score   │  │ - OCR (Text)     │
│              │  │ - Malware Check│  │ - TXT → PDF      │
└──────────────┘  └───────┬────────┘  └─────────┬────────┘
                           │                     │
                           ▼                     ▼

                ┌────────────────────────────────────┐
                │         Processing Layer           │
                │                                    │
                │ - Hash Generator                   │
                │ - SHA256 / SHA1 / MD5             │
                │ - Risk Analysis Engine            │
                │ - File Intelligence Scanner       │
                └──────────────────┬────────────────┘
                                   │
                                   ▼

                    ┌────────────────────────┐
                    │    Docker Container    │
                    │  (Portable Deployment) │
                    └─────────┬──────────────┘
                              │
                              ▼

                    ┌────────────────────────┐
                    │ GitHub Actions (CI/CD) │
                    │                        │
                    │ - Build & Test         │
                    │ - Docker Validation    │
                    │ - Automated Workflow   │
                    └─────────┬──────────────┘
                              │
                              ▼

                    ┌────────────────────────┐
                    │ Terraform (IaC Layer)  │
                    │                        │
                    │ - Infrastructure Setup │
                    │ - Local Simulation     │
                    └────────────────────────┘
```

---

## ▶️ Full Local Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

```bash
cd "SecureVault Pro – File Security & DevOps Project"
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

### Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Install OCR Engine (Tesseract)

### Windows

1. Download Tesseract OCR
2. Install it
3. Add Tesseract to PATH

Default path:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Optional inside `app.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

### 6️⃣ Run Flask Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t securevault-pro .
```

### Run Docker Container

```bash
docker run -p 5000:5000 securevault-pro
```

---

## ⚙️ Terraform Setup

### Open Terraform Folder

```bash
cd terraform
```

### Initialize Terraform

```bash
terraform init
```

### Apply Infrastructure

```bash
terraform apply
```

Type:

```text
yes
```

when prompted.

---

## 🔄 GitHub Actions CI/CD

The project includes a CI workflow that automatically:

- Checks out code
- Installs dependencies
- Tests Flask application
- Builds Docker image

Workflow file:

```text
.github/workflows/ci.yml
```

---

## 👨‍💻 Author

**Qaisar Rizwan Memar**  
Student at the American University of Afghanistan (AUAF)
