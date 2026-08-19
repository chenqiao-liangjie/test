# Hello World Module Design

## Problem Statement
Provide the canonical `hello world` function in Python. Per the spec, the
returned string must be **ALL UPPERCASE**.

## API
```python
def hello_world() -> str
```

- **Input:** none.
- **Output:** `"HELLO WORLD"` (fully uppercased).

## Key Decisions
1. **Return, don't print:** the function returns the string so it is testable
   and composable, matching the style of `src/farewell.py` and
   `src/chicken_rabbit.py`.
2. **Uppercase via literal:** the constant `"HELLO WORLD"` is written
   directly in uppercase rather than calling `"Hello World".upper()` —
   the expected output is fixed, so a literal is simpler and cannot drift.
3. **No parameters:** the spec asks for a plain hello world function; extra
   arguments are rejected by Python itself with a `TypeError`, so no manual
   validation is needed.
4. **Purity:** the function is deterministic and side-effect free; repeated
   calls always return the same string.

## Error Handling
- `hello_world("x")` → `TypeError` (unexpected argument, enforced by Python).

## Implementation Approach
Single function `hello_world()` in `src/hello_world.py` returning the
uppercase constant.
