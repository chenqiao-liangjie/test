# LCM (Least Common Multiple) Implementation Design

## Overview
Implement a Python function to calculate the least common multiple (LCM) of integers.

## Approach
- Use the mathematical relationship: `LCM(a, b) = |a * b| / GCD(a, b)`
- Support multiple integers by iteratively computing LCM
- Use Python's built-in `math.gcd` for GCD calculation

## Key Decisions
1. **Function signature**: `lcm(*numbers: int) -> int`
2. **Input validation**: 
   - Raise ValueError for empty input
   - Handle zero correctly (LCM of 0 and any number is 0)
   - Support negative numbers (return positive LCM)
3. **Edge cases**:
   - Single number returns absolute value
   - Zero in input returns 0
   - Negative numbers handled via absolute value

## Implementation Plan
1. Create `src/lcm.py` with main implementation
2. Export from `src/__init__.py`
3. Write comprehensive unit tests
