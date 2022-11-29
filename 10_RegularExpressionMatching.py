def isMatch(s: str, p: str) -> bool:
    si, pi = 0, 0 
    while si < len(s) and pi < len(p):
        star = pi + 1 < len(p) and p[pi+1] == "*"
        # .*
        if star and p[si] == ".":
            for k in range(pi, len(s) + 1):
                if isMatch(s[k:], p[si+2:]):
                    return True
            return False
        # .
        elif p[si] == ".":
            k += 1
        # (a-z)*
        elif star:
            for k in range(len(s) + 1):
                if isMatch(s[pi:], p[si] * k + p[si+2:]):
                    return True
            return False
        # a-z
        else:
            if p[si] == s[pi]:
                pi += 1
            else:
                return False
        si += 1
    while si + 1 < len(p) and p[si+1] == "*":
        si += 2
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