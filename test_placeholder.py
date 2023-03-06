import pytest
import requests
import json
from collections import namedtuple


@pytest.fixture(scope="module")
def fixt():
    print("started")
    yield {"initial": []}
    print("test ended")


@pytest.fixture
def fixt_new():
    print("start test")
    yield
    print("finish test")


def test_is_get_request_success(fixt, fixt_new):
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    # print("PRINT")
    # print(response.text)
    fixt["data"] = response.text
    assert response.status_code == 200


# def test_logo():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts")


def test_is_post_request_success():
    data = '{ "userId": 1, "title": "delectus aut autem", "body": "lorem ipsum"}'
    json_data = json.loads(data)
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json_data)
    response_obj = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    assert response.status_code == 201
    assert response_obj.body == "lorem ipsum"


def test_is_put_request_success():
    data = '{ "userId": 2, "title": "delectus aut autem", "body": "lorem ipsum"}'
    json_data = json.loads(data)
    response = requests.post("https://jsonplaceholder.typicode.com/posts/1", json_data)
    response_obj = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    assert response.status_code == 201
    assert response_obj.body == "lorem ipsum"


