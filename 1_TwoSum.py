"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    sumDict = {}
    for i in range(len(nums)):
        j = sumDict.get(nums[i])
        if j is None:
            sumDict[target - nums[i]] = i
        else:
            return [j, i]
        

print(twoSum([99,102,60,101,100,9,12,2], 69))
print(twoSum([0,0,3], 0))