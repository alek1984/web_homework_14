import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_contact():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/contacts/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1
