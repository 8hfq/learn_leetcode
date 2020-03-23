#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        p = root 
        while p.next and p.next.next:
            a= p.next
            b = a.next 
            p.next ,a.next,b.next = b , b.next, a 
            p = a
        return root.next
# @lc code=end

