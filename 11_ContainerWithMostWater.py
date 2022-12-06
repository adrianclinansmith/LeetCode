"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
- n == height.length
- 2 <= n <= 105
- 0 <= height[i] <= 104
"""

def maxArea(height: list[int]) -> int:
    maxAreaFound = 0
    maxHeightFound = 0
    i = 0
    j = len(height) - 1
    while i < j:
        currentHeight = min(height[i], height[j])
        if currentHeight > maxHeightFound:
            maxHeightFound = currentHeight
            maxAreaFound = max(maxAreaFound, currentHeight * (j - i))
        if height[i] <= maxHeightFound:
            i += 1
        if height[j] <= maxHeightFound:
            j -= 1
    return maxAreaFound
