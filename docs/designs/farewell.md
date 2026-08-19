# Farewell Module Design

## Problem Statement
Provide a simple greeting-style module with a `bye(name)` function that
returns the string `Goodbye, <name>!`.

## API
```python
def bye(name: str) -> str
```

- **Input:** `name` — the name of the person being farewelled.
- **Output:** `f"Goodbye, {name}!"`

## Key Decisions
1. **Return, don't print:** the function returns the string so it is testable
   and composable, matching the style of `src/chicken_rabbit.py`.
2. **Exact format:** `Goodbye, name!` — comma + space before the name, an
  exclamation mark at the end, capitalized "Goodbye".
3. **Type validation:** non-`str` inputs (e.g. `None`, `int`) raise
  `TypeError`, consistent with the explicit validation style used elsewhere
  in this codebase.
4. **Empty name:** an empty string is still a valid `str`; it produces
  `Goodbye, !` — no special casing needed for a trivial formatter.

## Error Handling
- `bye(123)` / `bye(None)` → `TypeError: name must be a string`

## Implementation Approach
Single function `bye(name)` in `src/farewell.py` returning the formatted
farewell string.
