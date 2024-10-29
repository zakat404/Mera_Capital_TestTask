from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_prices():
    response = client.get("/api/prices?ticker=btc_usd")
    assert response.status_code in [200, 404]

def test_get_latest_price():
    response = client.get("/api/latest_price?ticker=btc_usd")
    assert response.status_code in [200, 404]

def test_get_prices_in_range():
    response = client.get("/api/prices_in_range?ticker=btc_usd&start_date=1695000000&end_date=1696000000")
    assert response.status_code in [200, 404]
