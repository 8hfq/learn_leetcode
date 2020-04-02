#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (42.22%)
# Likes:    1653
# Dislikes: 199
# Total Accepted:    227.8K
# Total Submissions: 534.1K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[-1]
        h = len(triangle)
        for i in range(h-2,-1,-1):
            for j in range(0,i+1):
                res[j] = min(res[j],res[j+1]) +triangle[i][j]
        return res[0]
        
# @lc code=end

