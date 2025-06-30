import requests

response = requests.get("https://api.github.com")
# отправляет get запрос на указыннный адрес

print(response.json())