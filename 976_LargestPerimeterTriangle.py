"""
LeetCode 976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106
"""

def largestPerimeter(nums: list[int]) -> int: 
        nums.sort(reverse = True) 
        i = 0
        while len(nums) - i > 2 and nums[i] >= nums[i+1] + nums[i+2]:
            i += 1       
        return 0 if len(nums) - i < 3 else sum(nums[i:i + 3])
