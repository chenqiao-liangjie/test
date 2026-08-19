# Test Cases: Farewell Module

## Normal Cases

### Case 1: Simple Name
- **Input:** name="Alice"
- **Expected Output:** "Goodbye, Alice!"

### Case 2: Another Name
- **Input:** name="Bob"
- **Expected Output:** "Goodbye, Bob!"

### Case 3: Name With Spaces
- **Input:** name="Ada Lovelace"
- **Expected Output:** "Goodbye, Ada Lovelace!"

## Edge Cases

### Case 4: Empty String
- **Input:** name=""
- **Expected Output:** "Goodbye, !"

### Case 5: Unicode Name
- **Input:** name="世界"
- **Expected Output:** "Goodbye, 世界!"

### Case 6: Name With Punctuation / Whitespace Preserved As-Is
- **Input:** name="  Bob  "
- **Expected Output:** "Goodbye,   Bob  !" (no trimming; formatter is trivial)

## Error / Invalid Input Cases

### Case 7: None Input
- **Input:** name=None
- **Expected Output:** raises TypeError

### Case 8: Integer Input
- **Input:** name=123
- **Expected Output:** raises TypeError

### Case 9: Return Type Is str
- **Input:** name="Alice"
- **Expected Output:** isinstance(result, str) is True
