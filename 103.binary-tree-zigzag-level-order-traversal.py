#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (45.13%)
# Likes:    1665
# Dislikes: 86
# Total Accepted:    318.3K
# Total Submissions: 696.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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

#dfs
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res =[]
#         self.dfs(root,0,res)
#         for i in range(len(res)):
#             if i%2==0:
#                 res[i] =res[i][::-1]
#         return res
#     def dfs(self,root,index,res):
#         if not root:
#             return
#         if len(res) == index:
#             res.append([])
#         res[index].append(root.val)
#         if root.right:
#             self.dfs(root.right,index+1,res)
#         if root.left:
#             self.dfs(root.left,index+1,res)

#bfs
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        flag =1
        tmp = []
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp+=[node.val]
                if node.left:
                    stack+=[node.left]
                if node.right:
                    stack+=[node.right]
            res+=[tmp[::flag]]
            tmp=[]
            flag*=-1
        return res
# @lc code=end

