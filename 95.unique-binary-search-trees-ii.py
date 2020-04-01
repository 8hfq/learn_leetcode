#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (38.42%)
# Likes:    1811
# Dislikes: 146
# Total Accepted:    175.2K
# Total Submissions: 450.6K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n ==0:
            return []
        return self.dfs(1,n+1)
    def dfs(self,start,end):
        if start ==end :
            return None
        
        result =[]
        for i in range(start,end):
            for p in self.dfs(start,i) or [None]:
                for q in self.dfs(i+1,end) or [None]: 
                    node = TreeNode(i)
                    node.left = p
                    node.right = q
                    result.append(node)
        return result
        
# @lc code=end

