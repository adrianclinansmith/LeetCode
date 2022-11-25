def solution(S):
    numDeletions = 0
    numB = 0
    for ch in S:
        numB += int(ch == "B")
        if ch == "A":
            numDeletions = min(numDeletions + 1, numB)
    return numDeletions