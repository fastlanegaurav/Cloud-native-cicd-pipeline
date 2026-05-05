# ⚙️ CI/CD Pipeline with GitHub Actions

![Build](https://github.com/YOUR_USERNAME/cicd-github-actions/actions/workflows/build.yml/badge.svg)
![Test](https://github.com/YOUR_USERNAME/cicd-github-actions/actions/workflows/test.yml/badge.svg)
![Deploy](https://github.com/YOUR_USERNAME/cicd-github-actions/actions/workflows/deploy.yml/badge.svg)

A production-ready CI/CD pipeline that automatically **builds → tests → deploys** a Python Flask app to AWS EC2 using GitHub Actions and Docker Hub.

---

## 🏗️ Architecture

```
Developer pushes code
        │
        ▼
┌───────────────────┐
│   GitHub Actions  │
│                   │
│  1. test.yml      │  ← Run pytest + lint + Docker build test
│  2. build.yml     │  ← Build & push Docker image to Docker Hub
│  3. deploy.yml    │  ← SSH into EC2, pull & run new container
└───────────────────┘
        │
        ▼
┌───────────────────┐
│   AWS EC2         │  ← Runs the Docker container
│   Docker Hub      │  ← Stores Docker images
└───────────────────┘
```

---

## 📁 Project Structure

```
cicd-github-actions/
├── .github/
│   └── workflows/
│       ├── build.yml       # Build & push Docker image
│       ├── test.yml        # Run tests & linting
│       └── deploy.yml      # Deploy to AWS EC2
│
├── app/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── templates/
│       └── index.html      # Web UI
│
├── tests/
│   └── test_app.py         # Pytest test suite
│
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Local development
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start (Local)

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/cicd-github-actions.git
cd cicd-github-actions
```

### 2. Run with Docker Compose
```bash
docker-compose up --build
```
Visit → http://localhost:5000

### 3. Run without Docker
```bash
cd app
pip install -r requirements.txt
python app.py
```

### 4. Run tests
```bash
pip install pytest pytest-flask
pytest tests/ -v
```

---

## 🔐 GitHub Secrets Setup

Go to your repo → **Settings → Secrets and variables → Actions** and add:

| Secret Name | Description |
|---|---|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub Access Token (not password) |
| `AWS_ACCESS_KEY_ID` | AWS IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM user secret key |
| `AWS_REGION` | e.g. `us-east-1` |
| `EC2_HOST` | Your EC2 public IP or DNS |
| `EC2_USER` | SSH user (e.g. `ubuntu`) |
| `EC2_SSH_KEY` | Your EC2 private key (contents of `.pem` file) |

---

## ☁️ AWS EC2 Setup

### 1. Launch EC2 Instance
- AMI: **Ubuntu 22.04 LTS**
- Instance type: `t2.micro` (free tier)
- Security Group: Allow **port 22** (SSH) and **port 80** (HTTP)

### 2. Install Docker on EC2
```bash
ssh ubuntu@YOUR_EC2_IP

# Install Docker
sudo apt update && sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker

# Add ubuntu user to docker group (no sudo needed)
sudo usermod -aG docker ubuntu
```

### 3. Push code to main → pipeline runs automatically! 🎉

---

## 🔄 CI/CD Pipeline Flow

```
git push origin main
        │
        ├─▶ test.yml runs
        │       ├── Lint code (flake8)
        │       ├── Run pytest (12 tests)
        │       └── Build & test Docker image
        │
        ├─▶ build.yml runs (if tests pass)
        │       ├── Build multi-stage Docker image
        │       └── Push to Docker Hub (tagged with SHA + latest)
        │
        └─▶ deploy.yml runs (if build passes)
                ├── SSH into EC2
                ├── Pull new Docker image
                ├── Replace old container
                └── Health check ✅
```

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Web UI |
| `/health` | GET | Health check (used by CI) |
| `/api/info` | GET | App info as JSON |

**Health check response:**
```json
{
  "status": "healthy",
  "version": "abc1234",
  "environment": "production"
}
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python / Flask | Web application |
| Pytest | Unit testing |
| Flake8 | Code linting |
| Docker | Containerization |
| Docker Hub | Image registry |
| GitHub Actions | CI/CD automation |
| AWS EC2 | Cloud hosting |
| Gunicorn | Production WSGI server |

---

## 📚 Skills Demonstrated

- ✅ CI/CD pipeline design and implementation
- ✅ Docker multi-stage builds
- ✅ Automated testing in pipeline
- ✅ Secrets management with GitHub Secrets
- ✅ SSH-based deployment automation
- ✅ Zero-downtime container replacement
- ✅ Health checks at every stage
