# Test Cases: Chicken and Rabbit (鸡兔同笼)

## Normal Cases

### Case 1: Classic Example
- **Input:** heads=35, feet=94
- **Expected Output:** chickens=23, rabbits=12
- **Verification:** 23+12=35 heads, 23*2+12*4=46+48=94 feet ✓

### Case 2: All Chickens
- **Input:** heads=10, feet=20
- **Expected Output:** chickens=10, rabbits=0
- **Verification:** 10+0=10 heads, 10*2+0*4=20 feet ✓

### Case 3: All Rabbits
- **Input:** heads=5, feet=20
- **Expected Output:** chickens=0, rabbits=5
- **Verification:** 0+5=5 heads, 0*2+5*4=20 feet ✓

### Case 4: Mixed Small Numbers
- **Input:** heads=3, feet=8
- **Expected Output:** chickens=2, rabbits=1
- **Verification:** 2+1=3 heads, 2*2+1*4=4+4=8 feet ✓

## Edge Cases

### Case 5: Zero Heads (Empty Cage)
- **Input:** heads=0, feet=0
- **Expected Output:** chickens=0, rabbits=0

### Case 6: Single Animal
- **Input:** heads=1, feet=2
- **Expected Output:** chickens=1, rabbits=0

### Case 7: Single Rabbit
- **Input:** heads=1, feet=4
- **Expected Output:** chickens=0, rabbits=1

## Error / Invalid Input Cases

### Case 8: Odd Number of Feet (Impossible)
- **Input:** heads=5, feet=15
- **Expected Output:** None (15 is odd, impossible)

### Case 9: Too Few Feet (Below Minimum)
- **Input:** heads=10, feet=10
- **Expected Output:** None (minimum would be 20 for all chickens)

### Case 10: Too Many Feet (Above Maximum)
- **Input:** heads=5, feet=30
- **Expected Output:** None (maximum would be 20 for all rabbits)

### Case 11: Negative Heads
- **Input:** heads=-1, feet=10
- **Expected Output:** None or raise ValueError

### Case 12: Negative Feet
- **Input:** heads=5, feet=-10
- **Expected Output:** None or raise ValueError

### Case 13: Non-integer Inputs
- **Input:** heads=5.5, feet=16
- **Expected Output:** Handle gracefully (type error or conversion)
