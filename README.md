# Secure File Hash Generator

A Flask web application that generates MD5, SHA1, and SHA256 hashes for uploaded files.

## Technologies Used
- Flask
- Git
- Docker
- GitHub Actions
- Terraform

## Run Application

python app.py

## Docker

docker build -t hash-generator .
docker run -p 5000:5000 hash-generator

## Terraform

terraform init
terraform apply