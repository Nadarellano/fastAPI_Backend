import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBleGFtcGxlLmNvbSIsImV4cCI6MTc0MDQ0NDk3Mn0._Kd0r-ub7mM0zyLaWfXo6hGHxw70XZD3nptJ7A7Oy3U"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Prueba en /breeds/
response = requests.get("http://127.0.0.1:5000/api/v1/breeds/", headers=HEADERS)
print(response.json())

# Prueba en /dogs/
response = requests.get("http://127.0.0.1:5000/api/v1/dogs/", headers=HEADERS)
print(response.json())
