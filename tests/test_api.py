from app.main import app


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_predict_returns_price():
    client = app.test_client()
    resp = client.post("/predict", json={"ram": 8, "ssd": 512, "cpu_score": 7})
    assert resp.status_code == 200
    assert isinstance(resp.get_json()["price"], (int, float))
