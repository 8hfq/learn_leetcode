#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = head
        while cur:
            pre = dummy
            while pre.next and pre.next.val<cur.val:
                pre = pre.next
            temp = cur.next
            cur.next = pre.next 
            pre.next = cur
            cur = temp 
        return dummy.next
        
# @lc code=end

