"""
LeetCode 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from __future__ import annotations
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def initWithList(nums: list[int]) -> ListNode:
        listNode = ListNode(val=nums[0])
        previousNode = listNode
        for num in nums[1:]:
            nextNode = ListNode(val=num)
            previousNode.next = nextNode
            previousNode = nextNode
        return listNode

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    headNode = None
    previousNode = None
    carry = 0
    while l1 or l2 or carry == 1:
        num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        carry = int(num > 9)
        currentNode = ListNode(val = num % 10)
        if previousNode:
            previousNode.next = currentNode
        else:
            headNode = currentNode
        previousNode = currentNode
    return headNode



l1 = ListNode.initWithList([1,9,9])
l2 = ListNode.initWithList([1,1])
listNode = addTwoNumbers(l1, l2)
while listNode:
        print(listNode.val)
        listNode = listNode.next