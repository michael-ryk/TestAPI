import requests

class TestFirstAPI:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Mich"
        data = {'name':name}
        response = requests.get(url, params=data)

        # Verify that server respond with Ok
        assert response.status_code == 200, "Wrong response code"

        # Verify if dictionary contains key 'answer'
        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        # Verify value from key answer
        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"