"""
8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
6. Return the integer as the final result.

Note:
- Only the space character ' ' is considered a whitespace character.
- Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""

MAX_32 = 2147483647 # 2^31 - 1
MIN_32 = -2147483648 # -2^31

def atoi(s: str) -> int:
    s = s.lstrip(" ")
    if len(s) == 0:
        return 0
    result = 0
    negator = -1 if s[0] == "-" else 1
    i = int(s[0] == "-" or s[0] == "+")
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    return max(MIN_32, min(result * negator, MAX_32))
    
def test(s: str):
    print(f"{s : <10} = {atoi(s)}")

test("")
test("0")
test("1")
test("001")
test("0012")
test("-1")
test("-0012")
test("0012a")
test("  2")
test("a")
test(f"{MAX_32 + 12}")
test(f"{MIN_32 - 12}")

