import pytest

from apistar import App, Route, TestClient
from apistar_cors import CORSMixin


class App(CORSMixin, App):
    pass


def index():
    return {}


ROUTES = [Route("/", "GET", index)]


@pytest.fixture(scope="session")
def app():
    return App(routes=ROUTES)


@pytest.fixture
def client(app):
    return TestClient(app)


def test_can_gen_cors_response(client):
    # Given that I have an app w/ CORS mixed in
    # When I make an options request
    response = client.options("/", headers={
        "origin": "https://example.com",
        "access-control-request-method": "GET",
    })

    # Then I should get back a successful response
    assert response.status_code == 204

    # And the response should contain CORS headers
    assert response.headers == {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Max-Age": "86400",
    }
