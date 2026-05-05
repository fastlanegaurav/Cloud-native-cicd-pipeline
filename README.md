# CI-DI
A production-ready CI/CD pipeline that automatically builds → tests → deploys a Python Flask app to AWS EC2 using GitHub Actions and Docker Hub.
Push to main
     ↓
✅ Pre-Deploy Tests
   - Checkout code
   - Setup Python 3.11
   - Install dependencies
   - Run pytest
     ↓ (only if tests pass)
🚀 Deploy to EC2
   - Checkout code
   - Configure AWS credentials
   - Add SSH key
   - SSH into EC2:
       → Docker login
       → Pull latest image
       → Stop old container
       → Start new container
       → Health check
     ↓
📣 Notify Success / ❌ Notify Failure
