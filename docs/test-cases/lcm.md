# LCM Test Cases

## Normal Cases
1. **Two positive integers**: lcm(4, 6) = 12
2. **Two coprime numbers**: lcm(5, 7) = 35
3. **One number is multiple of other**: lcm(3, 9) = 9
4. **Multiple numbers**: lcm(2, 3, 4) = 12
5. **Large numbers**: lcm(12, 18, 24) = 72

## Edge Cases
1. **Single number**: lcm(5) = 5
2. **With zero**: lcm(0, 5) = 0
3. **All zeros**: lcm(0, 0) = 0
4. **Negative numbers**: lcm(-4, 6) = 12 (returns positive)
5. **Both negative**: lcm(-4, -6) = 12

## Error Handling
1. **Empty input**: lcm() should raise ValueError
2. **Non-integer input**: Should raise TypeError (if type checking added)

## Boundary Cases
1. **Number 1**: lcm(1, any) = any
2. **Same numbers**: lcm(7, 7) = 7
