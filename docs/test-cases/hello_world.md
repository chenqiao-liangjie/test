# Test Cases: Hello World Module

## Normal Cases

### Case 1: Return Value
- **Input:** (none)
- **Expected Output:** "HELLO WORLD"

### Case 2: Fully Uppercase
- **Input:** (none)
- **Expected Output:** result == result.upper() is True

### Case 3: Return Type Is str
- **Input:** (none)
- **Expected Output:** isinstance(result, str) is True

## Edge Cases

### Case 4: Deterministic Across Calls
- **Input:** two consecutive calls
- **Expected Output:** both results are equal

### Case 5: Non-Empty
- **Input:** (none)
- **Expected Output:** len(result) > 0

## Error / Invalid Input Cases

### Case 6: Unexpected Argument
- **Input:** hello_world("extra")
- **Expected Output:** raises TypeError (Python enforces the no-arg signature)
