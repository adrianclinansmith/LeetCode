"""
LeetCode 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:
    lastCharIndex = {}
    maxLen = 0
    start = 0
    for i, c in enumerate(s):
        start = max(start, lastCharIndex.get(c, -1) + 1)
        maxLen = max(maxLen, i + 1 - start)
        lastCharIndex[c] = i
    return maxLen

def test(s: str):
    print(f"{s}: {lengthOfLongestSubstring(s)}")

test("")
test("a")
test("aa")
test("aaa")
test("aaba")
test("abaa")
test("baaa")
test("baab")
test("baba")
test("bbaa")
test("ab")
test("abc")
test("abcdcefg")
test("a#############abcd########abcde")
