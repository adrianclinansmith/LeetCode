"""
1653. Minimum Deletions to Make String Balanced

You are given a string s consisting only of characters 'a' and 'b'.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'. Return the minimum number of deletions needed to make s balanced.

Constraints:
1 <= s.length <= 105
s[i] is 'a' or 'b'.
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