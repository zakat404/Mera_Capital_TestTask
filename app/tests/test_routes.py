# app/tests/test_routes.py

import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_all_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/currency", params={"ticker": "btc_usd"})
    assert response.status_code == 200
