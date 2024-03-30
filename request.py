import requests

url = 'https://localhost:5000'
r = requests.post(url)

print(r.json())
