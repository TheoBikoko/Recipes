import requests

data = requests.get("http://127.0.0.1:8000/")

print(data.text)