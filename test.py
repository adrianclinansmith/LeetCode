
"""
a?bcd?a?
"""

def solution(riddle: str) -> str:
    s = ""
    for i in range(len(riddle)):
        if riddle[i] != "?":
            s += riddle[i]
            continue
        c1 = "a" if i == 0 else s[-1]
        c2 = "a" if i == len(riddle) - 1 else riddle[i+1]
        if c1 != "a" and c2 != "a":
            s += "a"
        elif c1 != "b" and c2 != "b": 
            s += "b"
        else:
            s += "c"
    return s

def test(s: str):
    print(f"{s} -> {solution(s)}")

test("a?bcd?a?")
test("?")
test("????")
