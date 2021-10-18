import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture(name="test_client")
def test_client_fixture():
    client = TestClient(app)
    yield client
