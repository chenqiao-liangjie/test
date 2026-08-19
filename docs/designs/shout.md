# Shout Module Design

## Problem Statement
Provide a `shout(text)` function that returns the given text converted to
uppercase.

## API
```python
def shout(text: str) -> str
```

- **Input:** `text` — the string to shout.
- **Output:** `text.upper()`

## Key Decisions
1. **Location:** `utils/shout.py` as specified, creating a new `utils`
   top-level package (`utils/__init__.py`) alongside the existing `src`
   package. Tests import via `from utils.shout import shout`.
2. **Return, don't print:** the function returns the uppercased string so it
   is testable and composable, matching the style of `src/hello_world.py`
   and `src/farewell.py`.
3. **Type validation:** non-`str` inputs (e.g. `None`, `int`) raise
   `TypeError`, consistent with the explicit validation style used in
   `src/farewell.py`.
4. **Delegation to `str.upper()`:** Unicode, digits, punctuation, and
   whitespace semantics (e.g. `ß` → `SS`) are handled by the built-in
   `str.upper()`; no custom casing logic.

## Error Handling
- `shout(None)` / `shout(123)` → `TypeError: text must be a string`

## Implementation Approach
Single function `shout(text)` in `utils/shout.py` returning
`text.upper()`.
