def solution(s):
    numDeletions = 0
    numB = 0
    for c in s:
        numB += int(c == "B")
        if c == "A":
            numDeletions = min(numDeletions + 1, numB)
    return numDeletions