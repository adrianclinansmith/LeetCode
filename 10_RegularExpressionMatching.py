"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

def removeRedundancies(p: str) -> str:
    i = p.find(".*")
    while i > -1:
        j = i - 1
        while j > 0 and p[j] == "*":
            j -= 2
        k = i + 3
        while k < len(p) and p[k] == "*":
            k += 2
        p = f"{p[0 : j+1]}.*{p[k-1 : len(p)]}"
        i = p.find(".*", j + 2)
    i = p.find("*")
    while i > -1:
        if p[i-1] == ".":
            i = p.find("*", i+1)
            continue
        j = i + 2
        while j < len(p) and p[j] == "*" and p[j-1] == p[i-1]:
            j += 2
        p = f"{p[0 : i+1]}{p[j-1 : len(p)]}"
        i = p.find("*", i+1)
    return p 

def handleStar(s: str, p: str, i: int) -> bool:
    c = p[i] # extract the character
    p = p[i + 2 : ] # consume the star expression and everything before it
    if c == ".":
       for j in range(i, len(s) + 1):
            if isMatch(s[j : ], p):
                return True 
    else: # c == a-z
        for j in range(len(s) + 1):
            if isMatch(s[i : ], c * j + p):
                return True
    return False

def isMatch(s: str, p: str) -> bool:
    p = removeRedundancies(p)
    i = 0 
    while i < len(s) and i < len(p):
        if i + 1 < len(p) and p[i + 1] == "*":
            return handleStar(s, p, i)
        elif p[i] != "." and p[i] != s[i]:
            return False
        i += 1
    lenP = len(p)
    while i < lenP and p[lenP - 1] == "*":
        lenP -= 2
    return i == len(s) and i == lenP

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
