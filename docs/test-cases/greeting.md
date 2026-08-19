# Test Cases: Greeting Module

## Normal Cases

### Case 1: Typical Name
- **Input:** name="Alice"
- **Expected Output:** "Hello, Alice!"

### Case 2: Another Typical Name
- **Input:** name="Bob"
- **Expected Output:** "Hello, Bob!"

### Case 3: Unicode Name
- **Input:** name="世界"
- **Expected Output:** "Hello, 世界!"

### Case 4: Name With Spaces
- **Input:** name="Ada Lovelace"
- **Expected Output:** "Hello, Ada Lovelace!"

## Edge Cases

### Case 5: Empty String
- **Input:** name=""
- **Expected Output:** "Hello, !" (allowed boundary value)

### Case 6: Whitespace-Only Name
- **Input:** name=" "
- **Expected Output:** "Hello,  !" (no implicit stripping)

### Case 7: Long Name
- **Input:** name="A" * 1000
- **Expected Output:** "Hello, " + "A" * 1000 + "!"

## Error / Invalid Input Cases

### Case 8: None Input
- **Input:** name=None
- **Expected Output:** raises TypeError

### Case 9: Integer Input
- **Input:** name=42
- **Expected Output:** raises TypeError

### Case 10: List Input
- **Input:** name=["Alice"]
- **Expected Output:** raises TypeError

### Case 11: Return Type Check
- **Input:** name="Alice"
- **Expected Output:** result is an instance of `str`
