# Chicken and Rabbit in Same Cage (鸡兔同笼) Design

## Problem Statement
Given the total number of heads and feet, calculate the number of chickens and rabbits.

## Mathematical Model
- Let `c` = chickens, `r` = rabbits
- Each chicken: 1 head, 2 feet
- Each rabbit: 1 head, 4 feet

**Equations:**
```
c + r = heads (total heads)
2c + 4r = feet (total feet)
```

**Solution:**
```
c = 2 * heads - feet / 2
r = feet / 2 - heads
```

## Constraints & Validation
1. Both `heads` and `feet` must be non-negative integers (booleans rejected explicitly, since `bool` is a subclass of `int` in Python)
2. `feet` must be even (sum of even numbers)
3. Minimum feet: `2 * heads` (all chickens)
4. Maximum feet: `4 * heads` (all rabbits)
5. Result must yield non-negative integers for both c and r

## Error Handling
- Return `None` or raise exception for invalid inputs
- Handle edge cases: zero heads, impossible foot counts

## Implementation Approach
Single function `chicken_rabbit(heads, feet)` returning tuple `(chickens, rabbits)` or `None` if no valid solution.
