import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def headers():
    return {"Content-Type": "application/json; charset=UTF-8'"}


@pytest.fixture
def post_data():
    return {"title": "Test Title", "body": "Test Body", "userId": 1}


def test_put_post(headers, post_data):
    post_data["id"] = 1
    response = requests.put(f"{BASE_URL}/posts/1", json=post_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Title"


def test_patch_post(headers):
    data = {"title": "Updated Title"}
    response = requests.patch(f"{BASE_URL}/posts/1", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_post(headers):
    response = requests.delete(f"{BASE_URL}/posts/1", headers=headers)
    assert response.status_code == 200
    assert response.json() == {}
