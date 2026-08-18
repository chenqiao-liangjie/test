"""Unit tests for LCM (Least Common Multiple) function."""

import pytest
from src.lcm import lcm


class TestLCMNormalCases:
    """Test normal LCM calculations."""

    def test_two_positive_integers(self):
        assert lcm(4, 6) == 12

    def test_two_coprime_numbers(self):
        assert lcm(5, 7) == 35

    def test_one_number_multiple_of_other(self):
        assert lcm(3, 9) == 9

    def test_multiple_numbers(self):
        assert lcm(2, 3, 4) == 12

    def test_large_numbers(self):
        assert lcm(12, 18, 24) == 72


class TestLCMEdgeCases:
    """Test edge cases for LCM."""

    def test_single_number(self):
        assert lcm(5) == 5

    def test_with_zero(self):
        assert lcm(0, 5) == 0

    def test_all_zeros(self):
        assert lcm(0, 0) == 0

    def test_negative_numbers(self):
        assert lcm(-4, 6) == 12

    def test_both_negative(self):
        assert lcm(-4, -6) == 12


class TestLCMErrorHandling:
    """Test error handling for LCM."""

    def test_empty_input_raises_error(self):
        with pytest.raises(ValueError):
            lcm()


class TestLCMBoundaryCases:
    """Test boundary cases for LCM."""

    def test_with_one(self):
        assert lcm(1, 5) == 5
        assert lcm(1, 100) == 100

    def test_same_numbers(self):
        assert lcm(7, 7) == 7
