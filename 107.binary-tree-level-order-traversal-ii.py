#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (49.86%)
# Likes:    1121
# Dislikes: 202
# Total Accepted:    291.1K
# Total Submissions: 574.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
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

class Solution:
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    # dfs
    #     res=[]
    #     if not root:
    #         return res
    #     self.dfs(root,0,res)
    #     return res[::-1]


    # def dfs(self,root,index,res):
    #     if not root:
    #         return 
    #     if len(res)==index:
    #         res.append([])
    #     res[index].append(root.val)
    #     self.dfs(root.left,index+1,res)
    #     self.dfs(root.right,index+1,res)


    #bfs
        if not root:
            return []
        res = []
        stack = [root]
        tmp = []
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp+=[node.val]
                if node.left:
                    stack+=[node.left]
                if node.right:
                    stack+=[node.right]
            res +=[tmp]
            tmp=[]
        return res[::-1]
# @lc code=end

