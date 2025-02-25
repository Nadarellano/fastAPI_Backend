import requests

response = requests.post("http://127.0.0.1:5000/api/v1/auth/", json={"email": "admin@example.com", "password": "1234"})
print(response.json())
