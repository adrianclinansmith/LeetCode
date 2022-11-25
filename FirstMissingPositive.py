# First Missing Positive

def positivesToLeft(nums: list[int]) -> int:
    """ Given a list of integers, put all positives on the left and return the number of positives. """
    pivot = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            temp = nums[pivot]
            nums[pivot] = nums[i]
            nums[i] = temp
            pivot += 1
    return pivot

def firstMissingPositive(nums: list[int]) -> int:
    """ Given a list of integers, return the smallest positive that's not in the list. """
    numberOfPositives = positivesToLeft(nums)
    for i in range(numberOfPositives):
        j = abs(nums[i]) - 1
        if j < numberOfPositives:
            nums[j] = -abs(nums[j])
    for i in range(numberOfPositives):
        if nums[i] > 0:
            return i + 1
    return 1 if numberOfPositives == 0 else numberOfPositives + 1

lists = [ [1], [1, 2, 3, 4], [3,2,1], [9,12,-12,77], 
    [-1,1,2], [7,-12,4,-2,18,18,-7,-7,1,33,2,0,-1,0] 
]

for l in lists:
    print(f"{l}:")
    s = firstMissingPositive(l)
    print(f"{l}:")
    print(f"{s}\n")


