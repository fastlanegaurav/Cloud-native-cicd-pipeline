# 🚀 Production-Ready CI/CD Pipeline

A fully automated CI/CD pipeline that builds, tests, and deploys a Python Flask application to AWS EC2 using GitHub Actions, Docker, and Docker Hub.

Designed to simulate real-world DevOps deployment workflows with automated testing, containerization, infrastructure deployment, and deployment health validation.

---

## 🌐 Project Overview

This project demonstrates a modern DevOps workflow where every push to the `main` branch automatically triggers:

* Source code validation
* Automated testing with Pytest
* Docker image build & push
* Remote deployment to AWS EC2
* Container replacement with zero manual intervention
* Post-deployment health verification

The pipeline follows production-style CI/CD practices used in cloud-native engineering environments.

---

# 📐 Architecture Diagram

                ┌─────────────────┐
                │    Developer    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ GitHub Repository│
                └────────┬────────┘
                         │ Push to main
                         ▼
              ┌────────────────────┐
              │ GitHub Actions CI  │
              │ Build & Test Stage │
              └────────┬───────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
 ┌────────────────┐       ┌────────────────┐
 │ Install Python │       │ Run Pytest     │
 │ Dependencies   │       │ Automated Tests│
 └────────────────┘       └────────────────┘
                       │
                       ▼
              ┌────────────────────┐
              │ Docker Image Build │
              └────────┬───────────┘
                       │
                       ▼
              ┌────────────────────┐
              │ Push to Docker Hub │
              └────────┬───────────┘
                       │
                       ▼
              ┌────────────────────┐
              │ AWS EC2 Deployment │
              │ SSH Remote Deploy  │
              └────────┬───────────┘
                       │
                       ▼
              ┌────────────────────┐
              │ Docker Container   │
              │ Restart & Replace  │
              └────────┬───────────┘
                       │
                       ▼
              ┌────────────────────┐
              │ Health Check &     │
              │ Deployment Verify  │
              └────────────────────┘
```

---

# ⚙️ Tech Stack

## CI/CD

* GitHub Actions
* Docker Hub

## Cloud

* AWS EC2

## Backend

* Python
* Flask

## Containerization

* Docker
* Docker Compose

## Testing

* Pytest

---

# ✨ Key Features

* Automated CI/CD workflow
* Dockerized Flask application
* Automated test execution before deployment
* Secure EC2 deployment using SSH
* Containerized production deployment
* Health check validation
* GitHub Actions automation
* Production-style deployment pipeline

---

# 📂 Project Structure

```bash id="u5j0m5"
.
├── .github/workflows/
│   └── test.yml
├── app/
│   └── index.html
├── tests/
├── Dockerfile
├── docker-compose.yml
├── README.md
```

---

# 🔄 CI/CD Workflow

## ✅ Continuous Integration

Every push to `main` triggers:

1. Checkout source code
2. Setup Python 3.11
3. Install dependencies
4. Execute automated tests using Pytest

---

## 🚀 Continuous Deployment

If tests pass successfully:

1. Build Docker image
2. Push image to Docker Hub
3. Connect to AWS EC2 using SSH
4. Pull latest container image
5. Stop old running container
6. Deploy updated container
7. Run deployment health checks

---

# 📊 Engineering Highlights

| Feature              | Impact                                |
| -------------------- | ------------------------------------- |
| Automated Deployment | Reduced manual deployment overhead    |
| Containerization     | Consistent runtime environments       |
| Automated Testing    | Improved deployment reliability       |
| Health Checks        | Faster deployment validation          |
| CI/CD Automation     | Production-style engineering workflow |

---

# 🛠️ Local Development

Clone repository:

```bash id="mpm0l7"
git clone https://github.com/fastlanegaurav/CI-DI.git
```

Navigate to project:

```bash id="e8x0b7"
cd CI-DI
```

Run locally with Docker:

```bash id="cgnvpi"
docker-compose up --build
```

---

# 🎯 DevOps Concepts Demonstrated

* CI/CD Automation
* Infrastructure Deployment
* Container Orchestration Concepts
* Automated Testing
* Cloud Deployment
* Immutable Infrastructure
* Deployment Validation
* Production Deployment Workflow

---

# 👨‍💻 Author

Gaurav Kumar Singh

DevOps Engineer | AWS | Kubernetes | Docker | CI/CD | Terraform

* GitHub: https://github.com/fastlanegaurav
* Portfolio: https://gaurav-portfolio-navy.vercel.app/
