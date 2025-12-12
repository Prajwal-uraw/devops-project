import requests

def test_service2_home():
    response = requests.get("http://localhost:5001")
    assert response.status_code == 200
    assert response.text == "Hello from Service 2!"
