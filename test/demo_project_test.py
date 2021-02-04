import pytest

from demo_project import count, app


def test_count():
    assert {} == count("")

    assert {
        "h": 1,
        "e": 1,
        "l": 3,
        "o": 2,
        " ": 1,
        "w": 1,
        "r": 1,
        "d": 1,
        "!": 1,
    } == count("hello world!")


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_app(client):
    response = client.get('/')
    assert response.status_code == 400
    assert response.json == {'error': 'Please specify a query parameter'}

    response = client.get('/?query=hello')
    assert response.status_code == 200
    assert response.json == {
        'h': 1,
        'e': 1,
        'l': 2,
        'o': 1,
    }
