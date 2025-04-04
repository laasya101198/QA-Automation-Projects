# API Testing using Python & Postman
import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert isinstance(response.json(), list), "Response is not a list"
    
    print("Test Passed: GET /users returns a valid response")

def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    response = requests.post(url, json=user_data)
    
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    assert response.json()["name"] == user_data["name"], "User name mismatch"
    
    print("Test Passed: POST /users creates a new user successfully")

if __name__ == "__main__":
    test_get_users()
    test_create_user()
