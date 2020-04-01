#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (49.53%)
# Likes:    2679
# Dislikes: 99
# Total Accepted:    257.2K
# Total Submissions: 514.1K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
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
class Solution:
    def numTrees(self, n: int) -> int:
        res  =[0 for i in range(n+1)]
        res[0] = 1 
        for i in range(n+1):
            for j in range(i):
                res[i] += res[j] * res[i-j-1]
        return res[n]
        
# @lc code=end

