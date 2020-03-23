#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        current = root
        carry = 0
        nums = [l1, l2]
        while nums:
            val = sum(n.val for n in nums) + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next
            nums = [n.next for n in nums if n.next]
        if carry:
            current.next = ListNode(carry)
        return root.next


        
# @lc code=end

