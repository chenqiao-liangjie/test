import pytest
from src.chicken_rabbit import chicken_rabbit


class TestChickenRabbitNormalCases:
    def test_classic_example(self):
        assert chicken_rabbit(35, 94) == (23, 12)

    def test_all_chickens(self):
        assert chicken_rabbit(10, 20) == (10, 0)

    def test_all_rabbits(self):
        assert chicken_rabbit(5, 20) == (0, 5)

    def test_mixed_small_numbers(self):
        assert chicken_rabbit(3, 8) == (2, 1)


class TestChickenRabbitEdgeCases:
    def test_empty_cage(self):
        assert chicken_rabbit(0, 0) == (0, 0)

    def test_single_chicken(self):
        assert chicken_rabbit(1, 2) == (1, 0)

    def test_single_rabbit(self):
        assert chicken_rabbit(1, 4) == (0, 1)


class TestChickenRabbitInvalidInput:
    def test_odd_feet(self):
        assert chicken_rabbit(5, 15) is None

    def test_too_few_feet(self):
        assert chicken_rabbit(10, 10) is None

    def test_too_many_feet(self):
        assert chicken_rabbit(5, 30) is None

    def test_negative_heads(self):
        assert chicken_rabbit(-1, 10) is None

    def test_negative_feet(self):
        assert chicken_rabbit(5, -10) is None

    def test_non_integer_heads(self):
        with pytest.raises(TypeError):
            chicken_rabbit(5.5, 16)

    def test_non_integer_feet(self):
        with pytest.raises(TypeError):
            chicken_rabbit(5, 16.5)

    def test_boolean_inputs_rejected(self):
        with pytest.raises(TypeError):
            chicken_rabbit(True, 4)

    def test_large_numbers(self):
        assert chicken_rabbit(1_000_000, 3_000_000) == (500_000, 500_000)
