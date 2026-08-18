"""LCM (Least Common Multiple) implementation."""

from math import gcd
from functools import reduce


def lcm(*numbers: int) -> int:
    """
    Calculate the least common multiple of one or more integers.
    
    Args:
        *numbers: One or more integers
        
    Returns:
        The LCM as a positive integer
        
    Raises:
        ValueError: If no numbers are provided
    """
    if not numbers:
        raise ValueError("At least one number is required")
    
    def lcm_pair(a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // gcd(a, b)
    
    return reduce(lcm_pair, numbers)
