#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (32.24%)
# Likes:    2762
# Dislikes: 233
# Total Accepted:    287.8K
# Total Submissions: 884.3K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.current_max = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.current_max
    
    def dfs(self,root):
        if not root:
            return 0
        left = max(self.dfs(root.left),0)
        right = max(self.dfs(root.right),0)
        self.current_max = max(left+right+root.val,self.current_max)
        return max(left,right)+root.val

        
# @lc code=end

