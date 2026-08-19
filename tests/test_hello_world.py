import pytest
from src.hello_world import hello_world


class TestHelloWorldNormalCases:
    def test_return_value(self):
        assert hello_world() == "HELLO WORLD"

    def test_fully_uppercase(self):
        result = hello_world()
        assert result == result.upper()

    def test_returns_str(self):
        assert isinstance(hello_world(), str)


class TestHelloWorldEdgeCases:
    def test_deterministic_across_calls(self):
        assert hello_world() == hello_world()

    def test_non_empty(self):
        assert len(hello_world()) > 0


class TestHelloWorldInvalidInput:
    def test_unexpected_argument(self):
        with pytest.raises(TypeError):
            hello_world("extra")
