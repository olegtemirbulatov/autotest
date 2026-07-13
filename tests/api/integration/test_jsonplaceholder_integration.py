import pytest

from api.json_placeholder_api_client import JsonPlaceholderClient
from models.post import Post

TIMEOUT = 10


# HAPPY PATH
@pytest.mark.integration
@pytest.mark.api
def test_get_post(json_placeholder_client: JsonPlaceholderClient):
    response = json_placeholder_client.get_post(post_id=1)
    assert response.status_code == 200
    Post.model_validate(response.json())


@pytest.mark.integration
@pytest.mark.api
def test_get_posts_list(json_placeholder_client: JsonPlaceholderClient):
    response = json_placeholder_client.get_posts_list(userId=1)
    assert response.status_code == 200
    posts_list = response.json()
    isinstance(posts_list, list)
    for post in posts_list:
        Post.model_validate(post)


@pytest.mark.integration
@pytest.mark.api
def test_create_post(
    json_placeholder_client: JsonPlaceholderClient, post_creation_payload
):
    response = json_placeholder_client.create_post(**post_creation_payload)
    assert response.status_code == 201
    creation_post_result = Post.model_validate(response.json())

    # Поля совпадают с переданными
    assert creation_post_result.title == post_creation_payload["title"]
    assert creation_post_result.body == post_creation_payload["body"]
    assert creation_post_result.userId == post_creation_payload["userId"]


@pytest.mark.integration
@pytest.mark.api
def test_delete_post(json_placeholder_client: JsonPlaceholderClient):
    response = json_placeholder_client.delete_post(post_id=1)
    assert response.status_code == 200


# ERROR PATH
@pytest.mark.integration
@pytest.mark.api
@pytest.mark.parametrize("post_id", [-1, 0, 99999])
def test_get_post_failure(json_placeholder_client: JsonPlaceholderClient, post_id: int):
    with pytest.raises(ValueError, match="Передан несуществующий ID"):
        json_placeholder_client.get_post(post_id=post_id)  # Non existent ID
