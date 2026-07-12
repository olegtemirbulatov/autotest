import pytest
import httpx
from models.post import Post

URL = "https://jsonplaceholder.typicode.com/"
TIMEOUT = 30


@pytest.mark.api
def test_get_post(http_client: httpx.Client):
    response = http_client.get(url=f"{URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    Post.model_validate(response.json())


@pytest.mark.api
def test_get_posts_list(http_client: httpx.Client):
    response = http_client.get(url=f"{URL}/posts?userId=1", timeout=TIMEOUT)
    assert response.status_code == 200
    posts_list = response.json()
    assert isinstance(posts_list, list)
    for post in posts_list:
        Post.model_validate(post)


@pytest.mark.api
def test_create_post(http_client: httpx.Client):
    payload = {"title": "new post", "body": "body of the post", "userId": 1}
    response = http_client.post(url=f"{URL}/posts", json=payload, timeout=TIMEOUT)
    assert response.status_code == 201
    post_result = Post.model_validate(response.json())

    # Поля совпадают с переданными
    assert post_result.title == payload["title"]
    assert post_result.body == payload["body"]
    assert post_result.userId == payload["userId"]


@pytest.mark.api
def test_delete_post(http_client: httpx.Client):
    response = http_client.delete(url=f"{URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200
