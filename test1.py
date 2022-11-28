"""
1653. Minimum Deletions to Make String Balanced


"""

def solution(s):
    numDeletions = 0
    numB = 0
    for c in s:
        numB += int(c == "b")
        if c == "a":
            numDeletions = min(numDeletions + 1, numB)
    return numDeletions

print(solution("aababbab"))