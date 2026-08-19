import pytest
from utils.shout import shout


class TestShoutNormalCases:
    def test_lowercase_word(self):
        assert shout("hello") == "HELLO"

    def test_mixed_case_sentence(self):
        assert shout("Hello World") == "HELLO WORLD"

    def test_already_uppercase(self):
        assert shout("SHOUT") == "SHOUT"


class TestShoutEdgeCases:
    def test_empty_string(self):
        assert shout("") == ""

    def test_unicode_text(self):
        assert shout("héllo wörld") == "HÉLLO WÖRLD"

    def test_digits_punctuation_and_whitespace(self):
        assert shout("order 66 - ready?") == "ORDER 66 - READY?"

    def test_returns_str(self):
        assert isinstance(shout("hello"), str)


class TestShoutInvalidInput:
    def test_none_input(self):
        with pytest.raises(TypeError):
            shout(None)

    def test_integer_input(self):
        with pytest.raises(TypeError):
            shout(123)

    def test_list_input(self):
        with pytest.raises(TypeError):
            shout(["a", "b"])
