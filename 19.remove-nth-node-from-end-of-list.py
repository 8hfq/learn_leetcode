#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(-1)
        root.next = head
        l = r = root
        for i in range(n):
            r = r.next
        while r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return root.next

        
# @lc code=end

