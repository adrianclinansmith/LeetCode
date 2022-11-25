"""
LeetCode 6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

def zigzagConversion1(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    zigzag = []
    for r in range(0, numRows):
        i = r
        c = 1
        while i < len(s): 
            zigzag.append(s[i])
            a = 1 + int(r == 0 or r == numRows - 1) 
            b = (numRows - 1 - 2 * r) * int(a == 1 and c % 2 != 0)
            i = r + a * c * (numRows - 1) + b
            c += 1
    return "".join(zigzag) 

def zigzagConversion2(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    grid = [[""] * len(s) for r in range(numRows)]
    r, c = 0, 0
    goDown = False
    for i in range(len(s)):
        grid[r][c] = s[i]
        if r == 0 or r == numRows - 1:
            goDown = not goDown
        if goDown:
            r += 1
        else:
            r, c = r - 1, c + 1
    joinedRows = []
    [joinedRows.extend(r) for r in grid]
    return "".join(joinedRows)
        
def test(s: str, numRows: int):
    print(f"{s} ({numRows}) -> {zigzagConversion2(s, numRows)}")

test("abcdefg", 2)             # acegbdf
test("abcdefghijklmn", 3)      # aeimbdfhjlncgk
test("abcdefghijklmnopqrs", 4) # agmsbfhlnrceikoqdjp
test("abcdefghijklmnopqrs", 5) # aiqbhjprcgkosdflnem