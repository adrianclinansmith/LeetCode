def handleStar(s: str, si: int, p: str, pi: int) -> bool:
    c = p[pi] # extract the character
    p = p[pi+2:] # consume star expression
    if c == ".":
       for j in range(si, len(s) + 1):
            if isMatch(s[j:], p):
                return True 
    else: # c == a-z
        for j in range(len(s) + 1):
            if isMatch(s[si:], c * j + p):
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

print("*~*~*~*~*~*~*~\nFalse\n*~*~*~*~*~*~*~")
print("Alpha:")
test("abc", "abf")
test("abc", "ab")
test("ab", "abc")
print("Star:")
test("abc", "aaa*bc")
test("abc", "a*aabc")