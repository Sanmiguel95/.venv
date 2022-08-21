import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_route():
    response = client.get('/infoUsers/Douglas_Cronin')
    assert response.status_code == 200

