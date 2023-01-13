import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json; charset=UTF-8'"}


@pytest.fixture
def post_data():
    return {"title": "Test Title", "body": "Test Body", "userId": 1}


def test_get_posts(headers):
    response = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 100


def test_get_post(headers):
    response = requests.get(f"{BASE_URL}/posts/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_post_post(headers, post_data):
    response = requests.post(f"{BASE_URL}/posts", json=post_data, headers=headers)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Title"
