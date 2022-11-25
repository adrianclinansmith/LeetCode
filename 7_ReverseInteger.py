"""
LeetCode 7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:
-2^31 <= x <= 2^31 - 1
"""
MAX_32 = 2147483647 # 2^31 - 1
M = MAX_32 // 10

def reverse(x: int) -> int:
    negator = -1 if x < 0 else 1
    x *= negator
    result = 0
    while x > 0:
        if result > M:
            return 0
        result = result * 10 + x % 10
        x //= 10
    return result * negator

def test(x: int):
    print(f"{x} -> {reverse(x)}")
    print(f"{-x} -> {reverse(-x)}")

test(1)
test(10)
test(101)
test(105)
test(123)
test(9007)
test(2147483641)
test(147483647)
test(2147483212)
test(999999999)
test(2147483647)
test(2147483612)