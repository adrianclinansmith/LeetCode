"""
LeetCode 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

See:
Manacher's algorithm
Dynamic Programming
"""


def expandPalindrome(s: str, left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]
        
def longestPalindrome(s: str) -> str:
    longest = ""
    for i in range(len(s)):
        if len(longest) > 2 * (len(s) - 1 - i):
            break
        p1 = expandPalindrome(s, i, i)
        p2 = expandPalindrome(s, i, i + 1)
        p = p1 if len(p1) > len(p2) else p2
        longest = p if len(p) > len(longest) else longest
    return longest


def test(s: str):
    print(f"{s} -> {longestPalindrome(s)}")

print("*************\nEven:\n*************\n")
test("abcbf")
test("zbccba")
test("abcdcba")
test("abca")
test("abbaabba")
test("abbaabbaabbaabba")
test("aaaazzaaaazzaaaa")
test("aabbaabba")
test("ccbbccccccbba")
test("aabaabaa")
test("baffabccbaf")
test("baffabbbbaf")
test("baabccba")
test("ababcba")
test("acabaca")
test("fabccba")
test("aaa")