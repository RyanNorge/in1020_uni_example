from fastapi.testclient import TestClient

from server import app


test_client = TestClient(
    app=app,
    base_url="http://testserver",
    raise_server_exceptions=True,
    root_path="",
    backend="asyncio",
    backend_options=None,
    cookies=None,
    headers=None,
    follow_redirects=True,
    client=("testclient", 50000),
)


def test_root():
    response = test_client.get("/")
    assert response.json() == {"Hello": "World"}


def test_failing():
    assert False
