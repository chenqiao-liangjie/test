# Greeting Module Design

## Problem Statement
Provide a simple `greet(name)` function that returns the string `Hello, <name>!`.

## API
```
greet(name: str) -> str
```
- **Input:** a person's name as a string
- **Output:** `f"Hello, {name}!"`

Example: `greet("Alice")` -> `"Hello, Alice!"`

## Key Decisions
1. **Return, don't print:** the function returns the greeting string so it is
   composable and testable (matches the functional style of `src/chicken_rabbit.py`).
2. **No trailing newline:** the exclamation mark terminates the greeting; callers
   can add formatting themselves.
3. **Strict type check on `name`:** non-string input (e.g. `None`, `int`) raises
   `TypeError` with a clear message, mirroring the input validation convention
   already used in `chicken_rabbit`.
4. **Empty string is allowed:** `greet("")` returns `"Hello, !"` rather than
   erroring — an empty name is a boundary value, not an invalid type.

## Error Handling
| Input | Behavior |
| --- | --- |
| `"Alice"` | `"Hello, Alice!"` |
| `""` | `"Hello, !"` |
| `"World "` (whitespace kept) | `"Hello, World !"` — no implicit stripping; callers control normalization |
| `None`, `42`, `["A"]` | `TypeError("name must be a string")` |

## Implementation Approach
Single function `greet(name)` in `src/greeting.py` using an f-string. No
dependencies, no state.
