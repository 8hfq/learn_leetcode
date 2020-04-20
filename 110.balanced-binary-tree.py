#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (42.49%)
# Likes:    1906
# Dislikes: 150
# Total Accepted:    415.4K
# Total Submissions: 971K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#暴力解法 自上而下
# class Solution:
#     # Compute the tree's height via recursion
#     def height(self, root: TreeNode) -> int:
#         # An empty tree has height -1
#         if not root:
#             return -1
#         return 1 + max(self.height(root.left), self.height(root.right))
    
#     def isBalanced(self, root: TreeNode) -> bool:
#         # An empty tree satisfies the definition of a balanced tree
#         if not root:
#             return True

#         # Check if subtrees have height within 1. If they do, check if the
#         # subtrees are balanced
#         return abs(self.height(root.left) - self.height(root.right)) < 2 \
#             and self.isBalanced(root.left) \
#             and self.isBalanced(root.right)


#自下而上的解法 
class Solution:
    def isBalancedHelper(self,root):
        if not root:
            return True,-1 
        leftIsBalanced,leftHeight = self.isBalancedHelper(root.left)
      
        if not leftIsBalanced:
            return False,0
        rightIsBalanced,rightHeight = self.isBalancedHelper(root.right)
       
        if not rightIsBalanced:
            return False, 0
        return(abs(leftHeight-rightHeight)<2,1+max(leftHeight,rightHeight))
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
# @lc code=end

