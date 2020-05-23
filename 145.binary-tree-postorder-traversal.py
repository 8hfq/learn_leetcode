#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if root.left:
            self.dfs(root.left,res)
        if root.right:
            self.dfs(root.right,res)
        res.append(root.val)
        
# @lc code=end

