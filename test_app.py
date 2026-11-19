from app import app


def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "<h1>Shop</h1>" in response.text
def test_health():
    response = app.test_client().get("/health")
    assert response.json == {"status": "ok"}