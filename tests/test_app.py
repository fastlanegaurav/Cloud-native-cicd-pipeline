import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../app"))
from app import app as flask_app


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    flask_app.config["APP_ENV"] = "test"
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


# ── Health check ──────────────────────────────────────────────
class TestHealth:
    def test_health_returns_200(self, client):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_json(self, client):
        response = client.get("/health")
        data = response.get_json()
        assert data is not None

    def test_health_status_is_healthy(self, client):
        response = client.get("/health")
        data = response.get_json()
        assert data["status"] == "healthy"

    def test_health_has_version(self, client):
        response = client.get("/health")
        data = response.get_json()
        assert "version" in data

    def test_health_has_environment(self, client):
        response = client.get("/health")
        data = response.get_json()
        assert "environment" in data


# ── Home route ────────────────────────────────────────────────
class TestHome:
    def test_home_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_home_returns_html(self, client):
        response = client.get("/")
        assert b"CI/CD Demo App" in response.data


# ── API Info ──────────────────────────────────────────────────
class TestApiInfo:
    def test_info_returns_200(self, client):
        response = client.get("/api/info")
        assert response.status_code == 200

    def test_info_has_app_name(self, client):
        response = client.get("/api/info")
        data = response.get_json()
        assert data["app"] == "cicd-demo"

    def test_info_has_message(self, client):
        response = client.get("/api/info")
        data = response.get_json()
        assert "message" in data

    def test_invalid_route_returns_404(self, client):
        response = client.get("/does-not-exist")
        assert response.status_code == 404
