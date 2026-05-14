# 🔐 SecureVault Pro – File Security & DevOps Project

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![CI](https://img.shields.io/badge/GitHub%20Actions-CI%20Passing-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## 🚀 Project Overview

SecureVault Pro is a **Flask-based cybersecurity web application** that analyzes uploaded files for:

- MD5, SHA1, SHA256 hashing
- File type detection
- Risk scoring engine
- Basic malware detection (hash-based)
- Image to PDF conversion
- OCR (Image to Text simulation / optional real OCR support)

It is built as a **DevOps-integrated project** demonstrating the full workflow from development to deployment.

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
```text
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
                    │ - Docker validation     │
                    └─────────┬──────────────┘
                              ▼
                    ┌────────────────────────┐
                    │ Terraform (IaC Layer)  │
                    │ - Infrastructure setup │
                    └────────────────────────┘

---
## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app.py