import pytest
from src.farewell import bye


class TestByeNormalCases:
    def test_simple_name(self):
        assert bye("Alice") == "Goodbye, Alice!"

    def test_another_name(self):
        assert bye("Bob") == "Goodbye, Bob!"

    def test_name_with_spaces(self):
        assert bye("Ada Lovelace") == "Goodbye, Ada Lovelace!"


class TestByeEdgeCases:
    def test_empty_string(self):
        assert bye("") == "Goodbye, !"

    def test_unicode_name(self):
        assert bye("世界") == "Goodbye, 世界!"

    def test_surrounding_whitespace_preserved(self):
        assert bye("  Bob  ") == "Goodbye,   Bob  !"

    def test_returns_str(self):
        assert isinstance(bye("Alice"), str)


class TestByeInvalidInput:
    def test_none_input(self):
        with pytest.raises(TypeError):
            bye(None)

    def test_integer_input(self):
        with pytest.raises(TypeError):
            bye(123)
