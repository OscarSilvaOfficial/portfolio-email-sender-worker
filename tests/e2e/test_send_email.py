from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_send_mail_for_contact():
  json = {"email": "oscarkaka222@gmail.com", "message": "Test E2E", "name": "Kaka"}
  response = client.post("/contacts", json=json)
  assert response.status_code == 200
  assert response.json() == "OK"
  