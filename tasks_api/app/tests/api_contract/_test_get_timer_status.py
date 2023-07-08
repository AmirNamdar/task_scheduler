from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_timer_status():
    response = client.get("/timers/1")
    assert response.status_code == 200
    assert response.json() == {"id": "1", "time_left": 14401}
