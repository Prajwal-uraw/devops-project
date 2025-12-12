import requests

def test_service1_home():
    response = requests.get("http://localhost:5000")
    assert response.status_code == 200
    assert response.text == "Hello from Service 1!"
