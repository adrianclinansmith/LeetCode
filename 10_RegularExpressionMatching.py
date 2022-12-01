"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.​​​​
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

def handleStar(s: str, si: int, p: str, pi: int) -> bool:
    c = p[pi] # extract the character
    p = p[pi + 2 : ] # consume star expression
    if c == ".":
       for j in range(si, len(s) + 1):
            if isMatch(s[j : ], p):
                return True 
    else: # c == a-z
        for j in range(len(s) + 1):
            if isMatch(s[si : ], c * j + p):
                return True
    return False


def isMatch(s: str, p: str) -> bool:
    si, pi = 0, 0 
    while si < len(s) and pi < len(p):
        if pi + 1 < len(p) and p[pi + 1] == "*":
            return handleStar(s, si, p, pi)
        elif p[pi] != "." and p[pi] != s[si]:
            return False
        si += 1; pi += 1
    while pi + 1 < len(p) and p[pi + 1] == "*":
        pi += 2
    return si == len(s) and pi == len(p) 

def test(s, p):
    functionStr = f"isMatch({s}, {p})"
    print(f"{functionStr : <25} = {isMatch(s, p)}")

print("*~*~*~*~*~*~*~\nTrue\n*~*~*~*~*~*~*~")
print("Alpha:")
test("abc", "abc")
print("Star alpha:")
test("", "a*")
test("a", "a*")
test("aaa", "a*")
test("bc", "a*bc")
test("abc", "a*bc")
print("dot:")
test("a", ".")
test("abc", "...")
test("abc", "a.c")
print("dot star:")
test("a", ".*")
test("abcd", ".*")
test("", ".*")
test("", "a*.*.*b*")
test("abc", "a*.*.*b*")

print("*~*~*~*~*~*~*~\nFalse\n*~*~*~*~*~*~*~")
print("Alpha:")
test("abc", "abf")
test("abc", "ab")
test("ab", "abc")
print("Star:")
test("abc", "aaa*bc")
test("abc", "a*aabc")
print("dot:")
test("ab", ".")
test("abc", "..a")