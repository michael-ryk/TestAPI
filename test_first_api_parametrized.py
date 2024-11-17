import pytest
import requests

class TestFirstAPI:
    names = [
        ("Jhon"),
        ("Patric"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}
        response = requests.get(url, params=data)

        # Verify that server respond with Ok
        assert response.status_code == 200, "Wrong response code"

        # Verify if dictionary contains key 'answer'
        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        # Special case when no name passed and we expect default name
        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        # Verify value from key answer
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"