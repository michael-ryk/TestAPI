import pytest
import requests


class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        # Verify basic parameters received
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header"
        assert "user_id" in response1.json(), "There is no user id in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_auth = response1.json()['user_id']

    def test_auth_user(self):
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})

        # Verify response
        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_check = response2.json()["user_id"]

        assert self.user_id_auth == user_id_check, "User id from auth method not equal to user id from check method"


    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                     headers={"x-csrf-token": self.token})
        elif condition == "no_token":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                     cookies={"auth_sid": self.auth_sid})
        else:
            print("unknown case")
            response2 = "Null"

        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_check_method = response2.json()["user_id"]
        assert user_id_check_method == 0, f"User is authorized with condition {condition}"

