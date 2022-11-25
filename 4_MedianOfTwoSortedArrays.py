"""
LeetCode 4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from colorama import Fore
from typing import Callable

def binarySearch(toFind: int, nums: list[int], start: int, end: int) -> tuple[int, bool]:
    i = start
    while start < end:
        i = int((end - start) / 2) + start
        if toFind == nums[i]:
            return (i, True)
        elif toFind < nums[i]:
            end = i
        else:
            start = i + 1 
    if i >= len(nums):
        return (len(nums), False)
    return (i if toFind < nums[i] else i + 1, False)

def chooseValidElement(chooser: Callable[[int, int], int], nums1: list[int], i1: int, nums2: list[int], i2: int) -> int:
    if i1 < 0 or i1 >= len(nums1):
        return nums2[i2]
    elif i2 < 0 or i2 >= len(nums2):
        return nums1[i1]
    else:
        return chooser(nums1[i1], nums2[i2])


def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    start1, end1 = 0, len(nums1)
    start2, end2 = 0, len(nums2)
    i1 = int(len(nums1) / 2)
    while True:
        i2 = binarySearch(nums1[i1], nums2, start2, end2)[0]
        # i2 is the index of nums1[i1] if it was inserted into nums2
        rightSubLeft = (len(nums2) - i2 + len(nums1) - i1 - 1) - (i1 + i2)
        if rightSubLeft == 0:
            # nums1[i1] is the median
            return nums1[i1]
        elif rightSubLeft == -1:
            # nums1[i1] and the previous element are the median 
            previous = chooseValidElement(max, nums1, i1-1, nums2, i2-1)
            return (nums1[i1] + previous) / 2 
        elif rightSubLeft == 1:
            # nums1[i1] and the following element are the median 
            following = chooseValidElement(min, nums1, i1+1, nums2, i2)
            return (nums1[i1] + following) / 2 
        elif rightSubLeft < 0:
            # The median is somewhere to the left of nums1[i1]
            end1, end2 = i1, i2
        else:
            # The median is somewhere to the right of nums1[i1]
            start1, start2 = i1 + 1, i2
        nums1, nums2 = nums2, nums1
        start1, start2 = start2, start1
        end1, end2 = end2, end1
        stepSize = int(rightSubLeft / 2)
        i1 = i2 + stepSize - int(stepSize > 0)
        # Note that if nums1[i1] was inserted into nums2, the following element would be nums2[i2]

passes = 0
fails = 0

def test(nums1, nums2, repeat = True):
    nums = sorted(nums1 + nums2)
    i = int(len(nums) / 2)
    trueMedian = nums[i] if len(nums) % 2 != 0 else (nums[i - 1] + nums[i]) / 2
    myMedian = findMedianSortedArrays(nums1, nums2)
    if (abs(trueMedian - myMedian) < 0.001):
        print(Fore.GREEN + f"{trueMedian} == {myMedian}")
        global passes; passes = passes + 1
    else:
        print(Fore.RED + f"True: {trueMedian}, Mine: {myMedian}")
        global fails; fails = fails + 1
    print(Fore.WHITE)
    if repeat:
        test(nums2, nums1, False)

print("********************\nODD TESTS:\n********************\n")
test([30], [10, 20])
test([10], [20, 30])
# test([1,2,3], [1,2,3,4])
test([1, 3, 4, 6], [2, 4, 6])
test([-1, -3, -4, -6], [-2, -4, -6])
test([30], [60, 70, 80, 90, 100, 110, 120, 130])
test([10,30,50], [27,28,29,31])
test([10, 20, 30, 40, 50], [27, 28, 29, 31])
test([10, 20, 30, 40, 50], [28, 29, 31, 32, 33, 34])
test([10, 20, 30, 40, 50], [27, 28, 29, 31, 32, 33, 34, 35])
test([10, 20, 30, 40, 50], [27, 28, 29, 31, 32, 33, 34, 35, 36, 37])
test([1, 2, 3, 4, 5], [10, 11, 12, 13])
test([30, 40, 50], [60, 70, 80, 90, 100, 110, 120, 130])
test([30, 40, 50], [6, 7, 8, 9, 10, 11, 12, 130])
test([1, 3, 5], [2, 4, 6, 8])
test([30, 40, 50], [6, 7, 8, 9, 10, 11, 12, 130])
test([1,1,1,1], [1,1,1])
test([29, 30, 31, 32, 33, 34], [29, 30, 30, 31])
print("********************\nEVEN TESTS:\n********************\n")
test([1], [1])
test([1,2,3], [1,2,3])
test([1,2,3,4], [5,6,7,8])
test([1,3,5,7], [2,4,6,8])
test([-1], [-4,-2,1])
test([10, 20, 30, 40, 50], [29, 31, 32, 33, 34])
test([10, 20, 30, 40, 50], [28, 29, 31, 32, 33, 34, 35])
test([10, 20, 30, 40, 50], [28, 29, 31, 32, 33, 34, 35, 36, 37])
test([10, 20, 30, 40, 50], [27, 28, 29, 31, 32])
test([10, 20, 30, 40, 50], [28, 29, 31, 32, 33])
test([10, 29, 30, 40, 50], [20, 27, 28, 31, 32])
test([10, 29, 30, 31, 50], [28, 29, 32, 33, 40])
test([1,1,1,1], [1,1,1,1])

test([69], [])
test([70, 72], [])
print(f"Total: {passes} / {passes + fails}")
exit()

