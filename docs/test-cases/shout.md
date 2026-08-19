# Test Cases: Shout Module

## Normal Cases

### Case 1: Lowercase Word
- **Input:** text="hello"
- **Expected Output:** "HELLO"

### Case 2: Mixed Case Sentence
- **Input:** text="Hello World"
- **Expected Output:** "HELLO WORLD"

### Case 3: Already Uppercase (Idempotent)
- **Input:** text="SHOUT"
- **Expected Output:** "SHOUT"

## Edge Cases

### Case 4: Empty String
- **Input:** text=""
- **Expected Output:** ""

### Case 5: Unicode Text
- **Input:** text="héllo wörld"
- **Expected Output:** "HÉLLO WÖRLD"

### Case 6: Digits, Punctuation, And Whitespace Unchanged
- **Input:** text="order 66 - ready?"
- **Expected Output:** "ORDER 66 - READY?"

### Case 7: Return Type Is str
- **Input:** text="hello"
- **Expected Output:** isinstance(result, str) is True

## Error / Invalid Input Cases

### Case 8: None Input
- **Input:** text=None
- **Expected Output:** raises TypeError

### Case 9: Integer Input
- **Input:** text=123
- **Expected Output:** raises TypeError

### Case 10: List Input
- **Input:** text=["a", "b"]
- **Expected Output:** raises TypeError
