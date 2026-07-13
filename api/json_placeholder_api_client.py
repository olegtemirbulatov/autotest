import requests


class JsonPlaceholderClient:

    def __init__(self, session: requests.Session, timeout: int, base_url: str):
        self.session = session
        self.timeout = timeout
        self.base_url = base_url

    def get_post(self, post_id: int) -> requests.Response:
        url = f"{self.base_url}/posts/{post_id}"
        try:
            response = self.session.get(url=url, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Сервер не ответил за {self.timeout} секунд") from None
        except requests.exceptions.HTTPError as ex:
            if ex.response.status_code == 404:
                raise ValueError("Передан несуществующий ID") from ex
            raise

    def get_posts_list(self, userId: int = None) -> requests.Response:
        url = f"{self.base_url}/posts?userId={userId}"
        try:
            response = self.session.get(url=url, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Сервер не ответил за {self.timeout} секунд") from None
        except requests.exceptions.HTTPError as ex:
            if ex.response.status_code == 400:
                raise ValueError("Некорректные параметры запроса") from ex
            raise

    def create_post(self, title: str, body: str, userId: int) -> requests.Response:
        url = f"{self.base_url}/posts"
        payload = {"title": title, "body": body, "userId": userId}
        try:
            response = self.session.post(url=url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Сервер не ответил за {self.timeout} секунд") from None
        except requests.exceptions.HTTPError as ex:
            if ex.response.status_code == 400:
                raise ValueError("Неверные данные поста") from ex
            raise

    def delete_post(self, post_id: int) -> requests.Response:
        url = f"{self.base_url}/posts/{post_id}"
        try:
            response = self.session.delete(url=url, timeout=self.timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Сервер не ответил за {self.timeout} секунд") from None
        except requests.exceptions.HTTPError as ex:
            if ex.response.status_code == 404:
                raise ValueError("Передан несуществующий ID") from ex
            raise
