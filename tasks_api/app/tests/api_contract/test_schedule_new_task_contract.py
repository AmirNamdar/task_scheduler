from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_happy_path():
    response = client.post(
        "/timers",
        json={
            "hours": 4,
            "minutes": 0,
            "seconds": 1,
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["success"]
    assert "data" in response_data
    assert "id" in response_data["data"]
    assert "time_left" in response_data["data"]


def test_invalid_hours():
    response = client.post(
        "/timers",
        json={
            "hours": -1,
            "minutes": 0,
            "seconds": 1,
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
    )
    assert response.status_code == 400
    response_data = response.json()
    assert not response_data["success"]
    assert "data" in response_data
    assert response_data["data"]["field"] == "hours"
    assert "error_code" in response_data["data"]
    assert "message" in response_data["data"]


def test_invalid_minutes():
    response = client.post(
        "/timers",
        json={
            "hours": 4,
            "minutes": 60,
            "seconds": 1,
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
    )
    assert response.status_code == 400
    response_data = response.json()
    assert not response_data["success"]
    assert "data" in response_data
    assert response_data["data"]["field"] == "minutes"
    assert "error_code" in response_data["data"]
    assert "message" in response_data["data"]


def test_invalid_seconds():
    response = client.post(
        "/timers",
        json={
            "hours": 4,
            "minutes": 0,
            "seconds": 60,
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
    )
    assert response.status_code == 400
    response_data = response.json()
    assert not response_data["success"]
    assert "data" in response_data
    assert response_data["data"]["field"] == "seconds"
    assert "error_code" in response_data["data"]
    assert "message" in response_data["data"]


def test_invalid_url():
    response = client.post(
        "/timers",
        json={
            "hours": 4,
            "minutes": 0,
            "seconds": 1,
            "url": "bad url",
        },
    )
    assert response.status_code == 400
    response_data = response.json()
    assert not response_data["success"]
    assert "data" in response_data
    assert response_data["data"]["field"] == "url"
    assert "error_code" in response_data["data"]
    assert "message" in response_data["data"]
