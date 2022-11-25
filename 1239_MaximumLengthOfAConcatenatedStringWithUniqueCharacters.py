"""
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""

def uniqueChars(s: str):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def maxConcatWithUniqueChars(arr: list[str]) -> int:
    maxFound = 0
    def innerRecursive(arr: list[str]):
        nonlocal maxFound
        maxFound = max(maxFound, len(arr[0]))
        for i in range(1, len(arr)):
            if uniqueChars(arr[0] + arr[i]):
                innerRecursive([arr[0] + arr[i]] + arr[i+1:])
    for i in range(len(arr)):
        if uniqueChars(arr[i]):
            innerRecursive(arr[i:])
    return maxFound

def test(strings: list[str]):
    print(f"{strings}: {maxConcatWithUniqueChars(strings)}")

test(["abc", "xxxxxxxxxxxxxxxxxxx", "def", "abcd", "efgh"])
test(["abcdefg", "ab", "c", "de", "fg", "fghijkl"])
test(["abcdefghijklmnopqrstuvwxyz"])