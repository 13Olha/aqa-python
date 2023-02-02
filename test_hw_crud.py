import requests
import logging
from assertpy import assert_that
import pytest


BASE_URL = "https://reqres.in"


# logger setup
# https://stackoverflow.com/a/73158937
# https://stackoverflow.com/a/47447444
logger = logging.getLogger()
# logger_handler = logging.StreamHandler()  # console logger
logger_handler = logging.FileHandler("test.log", "a")  # logging into the file
for handler in logger.handlers[:]:  # remove old handlers
    if isinstance(handler, logging.FileHandler):
        logger.removeHandler(handler)
logger.addHandler(logger_handler)
logger.setLevel(logging.WARNING)


@pytest.fixture(autouse=True, scope="module")
def change_data():
    return {}


@pytest.fixture
def headers():
    return {"Content-Type": "application/json; charset=UTF-8'"}


@pytest.fixture
def upsert_data():
    return {"name": "morpheus", "job": "leader"}


def test_get(headers):
    response = requests.get(f"{BASE_URL}/api/users?page=2", headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["page"] == 2
    assert_that(response_data).contains_key("total_pages")


def test_get_users(headers):
    response = requests.get(f"{BASE_URL}/api/users/2", headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert_that(response_data).contains_key("data")
    assert response_data["data"]["id"] == 2


def test_post_users(headers, upsert_data):
    response = requests.post(f"{BASE_URL}/api/users", json=upsert_data, headers=headers)
    response_data = response.json()
    assert response.status_code == 201
    assert_that(response_data).contains_key("createdAt")


def test_put_users(headers, upsert_data):
    response = requests.put(f"{BASE_URL}/api/users/2", json=upsert_data, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert_that(response_data).contains_key("updatedAt")


def test_delete_user(headers):
    response = requests.delete(f"{BASE_URL}/api/users/2", headers=headers)
    assert response.status_code == 204
