"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Constraints:
-2^31 <= x <= 2^31 - 1
Follow up: Could you solve it without converting the integer to a string?
"""

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    xCopy = x
    reverse = 0
    while x > 0:
        reverse = reverse * 10 + x % 10
        x //= 10
    return xCopy == reverse

print(f"{121} -> {isPalindrome(121)}")
print(f"{321} -> {isPalindrome(321)}")