#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur ,pre = head,dummy
        for i in range(m-1):
            cur = cur.next
            pre = pre.next
        for i in range(n-m):
            temp = cur.next 
            cur.next = temp.next
            temp.next =pre.next
            pre.next =temp
        return dummy.next
# @lc code=end

