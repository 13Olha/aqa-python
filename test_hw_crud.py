import requests
import logging
from assertpy import assert_that
import pytest


URL = "https://reqres.in"


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


def test_get(change_data):
    response = requests.get(f"{URL}/api/users?page=2")
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["page"] == 2
    assert_that(response_data).contains_key("total_pages")


def test_get_users(change_data):
    response = requests.get(f"{URL}/api/users/2")
    response_data = response.json()
    assert response.status_code == 200
    assert_that(response_data).contains_key("data")
    assert response_data["data"]["id"] == 2


def test_post_users(change_data):
    post_data = '{"name": "morpheus", "job": "leader"}'
    response = requests.post(f"{URL}/api/users", post_data)
    response_data = response.json()
    assert response.status_code == 201
    assert_that(response_data).contains_key("createdAt")


def test_put_users():
    put_data = '{"name": "morpheus", "job": "leader"}'
    response = requests.put(f"{URL}/api/users/2", put_data)
    response_data = response.json()
    assert response.status_code == 200
    assert_that(response_data).contains_key("updatedAt")


def test_delete_user():
    response = requests.delete(f"{URL}/api/users/2")
    assert response.status_code == 204
