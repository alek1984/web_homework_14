import pytest
from fastapi.testclient import TestClient
from myapp.main import app

client = TestClient(app)

def test_get_quotes():
    response = client.get("/quotes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_quote():
    new_quote = {"text": "New Quote", "author": "Test Author"}
    response = client.post("/quotes/", json=new_quote)
    assert response.status_code == 201
    assert response.json()["text"] == "New Quote"

