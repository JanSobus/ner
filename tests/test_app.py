from app import create_app
from pytest import fixture

@fixture
def app():
    app = create_app()
    with app.app_context():
        app.config['WTF_CSRF_ENABLED'] = False
        yield app

@fixture
def client(app):
    return app.test_client()

@fixture
def runner(app):
    return app.test_cli_runner()

def test_main_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Input text" in response.data
    assert b"Find named entities" in response.data

def test_main_post(client):
    response = client.post('/', data={'sequence': 'John Smith lives in New York'})
    assert response.status_code == 200
    assert b"John Smith" in response.data
    assert b"New York" in response.data
    print(response.data)
    assert b"btn btn-danger" in response.data #PER button
    assert b"btn btn-success" in response.data #LOC button