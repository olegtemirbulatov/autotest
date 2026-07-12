import requests
import pytest


URL = "https://some_url"


@pytest.mark.skip(reason="This is a sample test")
@pytest.mark.api
def test_get_users():
    response = requests.get(f"{URL}/api/users?page=2")
    assert response.status_code == 200
    assert response.json()["body"] == "some value"


@pytest.mark.skip(reason="This is a sample test")
@pytest.mark.api
def test_login(login_credentials):
    response = requests.post(f"{URL}/api/login", json=login_credentials)
    assert response.status_code == 200
    assert response.json()["token"]