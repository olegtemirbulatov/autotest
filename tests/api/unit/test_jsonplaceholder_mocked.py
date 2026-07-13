import pytest
import requests
import responses
from models.post import Post

URL = "https://jsonplaceholder.typicode.com/"
TIMEOUT = 10


# MOCKED TESTS
@responses.activate
@pytest.mark.api
def test_get_post_mocked(http_session: requests.Session):
    responses.add(responses.GET,
                  f"{URL}/posts/1",
                  json={"userId": 1, "id": 1, "title": "Mocked", "body": "Test"},
                  status=200)

    response = http_session.get(url=f"{URL}/posts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    Post.model_validate(response.json())

    # Проверяем, что было обращение к замокированному ресурсу
    assert len(responses.calls) == 1