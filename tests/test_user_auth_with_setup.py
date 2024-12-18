import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self):
        # Before running any tests, we want see first we have auth_sid, token and user Id
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        # Verify basic parameters received
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_auth = self.get_json_value(response1, "user_id")


    def test_auth_user(self):
        # Positive test to check correct response
        response2 = MyRequests.get("/user/auth",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid}
                                   )

        # Verify using static method from my Assertions package
        Assertions.assert_json_value_by_name(response2, "user_id", self.user_id_auth,
        "User id from auth method not equal to user id from check method")

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        # 2 negative tests
        if condition == "no_cookie":
            response2 = MyRequests.get("/user/auth", headers={"x-csrf-token": self.token})

        elif condition == "no_token":
            response2 = MyRequests.get("/user/auth", cookies={"auth_sid": self.auth_sid})

        else:
            print("unknown case")
            response2 = "Null"

        # Verify using static method from my Assertions package
        Assertions.assert_json_value_by_name(response2, "user_id", 0,
        f"User is authorized with condition {condition}")


