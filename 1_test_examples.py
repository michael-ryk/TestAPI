class TestExample:
    def test_true_math(self):
        a = 5
        b = 9
        expect_sum = 14
        assert a+b == expect_sum, f"Sum of variables a and b is not as expected {expect_sum}"

    def test_false_math(self):
        a = 5
        b = 10
        expect_sum = 14
        assert a+b == expect_sum, f"Sum of variables a and b is not as expected {expect_sum}"