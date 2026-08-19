import pytest
from src.greeting import greet


class TestGreetNormalCases:
    def test_typical_name(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_another_typical_name(self):
        assert greet("Bob") == "Hello, Bob!"

    def test_unicode_name(self):
        assert greet("世界") == "Hello, 世界!"

    def test_name_with_spaces(self):
        assert greet("Ada Lovelace") == "Hello, Ada Lovelace!"


class TestGreetEdgeCases:
    def test_empty_string(self):
        assert greet("") == "Hello, !"

    def test_whitespace_only_name(self):
        assert greet(" ") == "Hello,  !"

    def test_long_name(self):
        name = "A" * 1000
        assert greet(name) == f"Hello, {name}!"


class TestGreetInvalidInput:
    def test_none_input(self):
        with pytest.raises(TypeError):
            greet(None)

    def test_integer_input(self):
        with pytest.raises(TypeError):
            greet(42)

    def test_list_input(self):
        with pytest.raises(TypeError):
            greet(["Alice"])

    def test_returns_str(self):
        assert isinstance(greet("Alice"), str)
