import pytest
import requests
import responses
from models.post import Post

URL = "https://jsonplaceholder.typicode.com/"
TIMEOUT = 10


def create_post(session: requests.Session, title: str, body: str, userId: int):
    url = f"{URL}/posts"
    payload = {"title": title, "body": body, "userId": userId}
    try:
        response = session.post(url=url, json=payload, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Сервер не ответил за {TIMEOUT} секунд") from None
    except requests.exceptions.HTTPError as ex:
        if ex.response.status_code == 400:
            raise ValueError("Неверные данные поста") from ex
        raise


@pytest.mark.api
def test_get_post(http_session: requests.Session):
    try:
        response = http_session.get(url=f"{URL}/posts/1", timeout=TIMEOUT)
        assert response.status_code == 200
        Post.model_validate(response.json())
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Сервер не ответил за {TIMEOUT} секунд") from None


@pytest.mark.api
def test_get_posts_list(http_session: requests.Session):
    try:
        response = http_session.get(url=f"{URL}/posts?userId=1", timeout=TIMEOUT)
        assert response.status_code == 200
        posts_list = response.json()
        assert isinstance(posts_list, list)
        for post in posts_list:
            Post.model_validate(post)
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Сервер не ответил за {TIMEOUT} секунд") from None


@pytest.mark.api
def test_create_post(http_session: requests.Session, post_creation_payload):
    post_result = Post.model_validate(
        create_post(session=http_session, **post_creation_payload)
    )

    # Поля совпадают с переданными
    assert post_result.title == post_creation_payload["title"]
    assert post_result.body == post_creation_payload["body"]
    assert post_result.userId == post_creation_payload["userId"]


@pytest.mark.api
def test_delete_post(http_session: requests.Session):
    try:
        response = http_session.delete(url=f"{URL}/posts/1", timeout=TIMEOUT)
        response.raise_for_status()
        assert response.status_code == 200
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Сервер не ответил за {TIMEOUT} секунд") from None
