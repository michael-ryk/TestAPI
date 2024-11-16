import requests

payload = {"name": "User"}

# Send Get request
get_response = requests.get("https://playground.learnqa.ru/api/check_type", params=payload)
print(get_response.text)

# Send post request
post_response = requests.post("https://playground.learnqa.ru/api/check_type", params=payload)
print(post_response.text)