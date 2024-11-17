import requests

# Receive cookie
payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
received_cookie = response1.cookies.get('auth_cookie')
print(f"Received Cookie: {received_cookie}")

# Send cookie
cookie_to_send = {}
if received_cookie is not None:
    cookie_to_send.update({'auth_cookie': received_cookie})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookie_to_send)
print(response2.text)