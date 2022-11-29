def isMatch(s: str, p: str) -> bool:
    si, pi = 0, 0 
    while si < len(s) and pi < len(p):
        nextIsStar = pi + 1 < len(p) and p[pi+1] == "*"
        # .*
        if nextIsStar and p[pi] == ".":
            for j in range(si, len(s) + 1):
                if isMatch(s[j:], p[pi+2:]):
                    return True
            return False
        # .
        elif p[pi] == ".":
            k += 1
        # (a-z)*
        elif nextIsStar:
            for j in range(len(s) + 1):
                if isMatch(s[si:], p[pi] * j + p[si+2:]):
                    return True
            return False
        # a-z
        else:
            if p[pi] == s[si]:
                si += 1
            else:
                return False
        pi += 1
    while pi + 1 < len(p) and p[pi+1] == "*":
        pi += 2
    return si == len(s) and pi == len(p) 

def test(s, p):
    print(f"isMatch({s}, {p}) = {isMatch(s, p)}")

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