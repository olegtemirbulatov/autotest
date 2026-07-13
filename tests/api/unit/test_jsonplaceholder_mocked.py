import pytest
import requests
import responses

from api.json_placeholder_api_client import JsonPlaceholderClient
from models.post import Post

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10

pytestmark = [pytest.mark.api, pytest.mark.mocked]


# ---------- get_post ----------


@responses.activate
def test_get_post_mocked(json_placeholder_client: JsonPlaceholderClient):
    mock_post = {"id": 1, "title": "Test title", "body": "Test body", "userId": 1}
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts/1",
        json=mock_post,
        status=200,
    )

    response = json_placeholder_client.get_post(post_id=1)

    assert response.status_code == 200
    Post.model_validate(response.json())
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.endswith("/posts/1")


@responses.activate
def test_get_post_not_found_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts/999999999",
        status=404,
    )

    with pytest.raises(ValueError, match="Передан несуществующий ID"):
        json_placeholder_client.get_post(post_id=999999999)


@responses.activate
def test_get_post_server_error_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts/1",
        status=500,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        json_placeholder_client.get_post(post_id=1)


@responses.activate
def test_get_post_timeout_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts/1",
        body=requests.exceptions.Timeout(),
    )

    with pytest.raises(RuntimeError, match=f"Сервер не ответил за {TIMEOUT} секунд"):
        json_placeholder_client.get_post(post_id=1)


# ---------- get_posts_list ----------


@responses.activate
def test_get_posts_list_mocked(json_placeholder_client: JsonPlaceholderClient):
    mock_posts = [
        {"id": 1, "title": "Title 1", "body": "Body 1", "userId": 1},
        {"id": 2, "title": "Title 2", "body": "Body 2", "userId": 1},
    ]
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts",
        json=mock_posts,
        status=200,
    )

    response = json_placeholder_client.get_posts_list(userId=1)

    assert response.status_code == 200
    posts_list = response.json()
    assert isinstance(posts_list, list)
    for post in posts_list:
        Post.model_validate(post)
    assert responses.calls[0].request.params == {"userId": "1"}


@responses.activate
def test_get_posts_list_empty_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts",
        json=[],
        status=200,
    )

    response = json_placeholder_client.get_posts_list(userId=999999999)

    assert response.status_code == 200
    assert response.json() == []


@responses.activate
def test_get_posts_list_invalid_params_mocked(
    json_placeholder_client: JsonPlaceholderClient,
):
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts",
        status=400,
    )

    with pytest.raises(ValueError, match="Некорректные параметры запроса"):
        json_placeholder_client.get_posts_list(userId=-1)


@responses.activate
def test_get_posts_list_timeout_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts",
        body=requests.exceptions.Timeout(),
    )

    with pytest.raises(RuntimeError, match=f"Сервер не ответил за {TIMEOUT} секунд"):
        json_placeholder_client.get_posts_list(userId=1)


# ---------- create_post ----------


@responses.activate
def test_create_post_mocked(
    json_placeholder_client: JsonPlaceholderClient, post_creation_payload
):
    mock_response = {**post_creation_payload, "id": 101}
    responses.add(
        responses.POST,
        f"{BASE_URL}/posts",
        json=mock_response,
        status=201,
    )

    response = json_placeholder_client.create_post(**post_creation_payload)

    assert response.status_code == 201
    result = Post.model_validate(response.json())
    assert result.title == post_creation_payload["title"]
    assert result.body == post_creation_payload["body"]
    assert result.userId == post_creation_payload["userId"]

    # Проверяем, что тело запроса ушло корректно
    import json

    sent_body = json.loads(responses.calls[0].request.body)
    assert sent_body == post_creation_payload


@responses.activate
def test_create_post_invalid_data_mocked(
    json_placeholder_client: JsonPlaceholderClient,
):
    responses.add(
        responses.POST,
        f"{BASE_URL}/posts",
        status=400,
    )

    with pytest.raises(ValueError, match="Неверные данные поста"):
        json_placeholder_client.create_post(title="", body="Test", userId=1)


@responses.activate
def test_create_post_server_error_mocked(
    json_placeholder_client: JsonPlaceholderClient, post_creation_payload
):
    responses.add(
        responses.POST,
        f"{BASE_URL}/posts",
        status=500,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        json_placeholder_client.create_post(**post_creation_payload)


@responses.activate
def test_create_post_timeout_mocked(
    json_placeholder_client: JsonPlaceholderClient, post_creation_payload
):
    responses.add(
        responses.POST,
        f"{BASE_URL}/posts",
        body=requests.exceptions.Timeout(),
    )

    with pytest.raises(RuntimeError, match=f"Сервер не ответил за {TIMEOUT} секунд"):
        json_placeholder_client.create_post(**post_creation_payload)


# ---------- delete_post ----------


@responses.activate
def test_delete_post_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/posts/1",
        json={},
        status=200,
    )

    response = json_placeholder_client.delete_post(post_id=1)

    assert response.status_code == 200
    assert len(responses.calls) == 1


@responses.activate
def test_delete_post_not_found_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/posts/999999999",
        status=404,
    )

    with pytest.raises(ValueError, match="Передан несуществующий ID"):
        json_placeholder_client.delete_post(post_id=999999999)


@responses.activate
def test_delete_post_server_error_mocked(
    json_placeholder_client: JsonPlaceholderClient,
):
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/posts/1",
        status=500,
    )

    with pytest.raises(requests.exceptions.HTTPError):
        json_placeholder_client.delete_post(post_id=1)


@responses.activate
def test_delete_post_timeout_mocked(json_placeholder_client: JsonPlaceholderClient):
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/posts/1",
        body=requests.exceptions.Timeout(),
    )

    with pytest.raises(RuntimeError, match=f"Сервер не ответил за {TIMEOUT} секунд"):
        json_placeholder_client.delete_post(post_id=1)
