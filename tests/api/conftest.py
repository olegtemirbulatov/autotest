from collections.abc import Generator
from typing import Dict

import pytest
import requests

from api.json_placeholder_api_client import JsonPlaceholderClient

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


@pytest.fixture()
def http_session() -> Generator[requests.Session, None, None]:
    with requests.Session() as session:
        yield session


@pytest.fixture()
def post_creation_payload() -> Generator[Dict[str, str | int], None, None]:
    payload: Dict[str, str | int] = {
        "title": "new post",
        "body": "body of the post",
        "userId": 1,
    }
    yield payload


@pytest.fixture()
def json_placeholder_client(http_session: requests.Session) -> JsonPlaceholderClient:
    return JsonPlaceholderClient(
        session=http_session, timeout=TIMEOUT, base_url=BASE_URL
    )
