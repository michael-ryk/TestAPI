import requests

# Receive response in JSON format
payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response = response.json()
print(parsed_response["answer"])        # Get specific key
print(parsed_response.get("answer"))    # Prevent error if key doesn't exists