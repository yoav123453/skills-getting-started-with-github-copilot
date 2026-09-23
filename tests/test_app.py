from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in payload["participants"]


def test_unregister_participant_missing_email_returns_404():
    activity_name = "Chess Club"
    email = "missing@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 404
