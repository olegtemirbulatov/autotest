import pytest
import requests


@pytest.fixture()
def http_session():
    with requests.Session() as session:
        yield session


@pytest.fixture()
def post_creation_payload():
    payload = {"title": "new post", "body": "body of the post", "userId": 1}
    yield payload