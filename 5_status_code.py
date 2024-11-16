import requests

response = requests.get("https://playground.learnqa.ru/api/check_type")
print(response.status_code)