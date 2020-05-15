#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (46.88%)
# Likes:    728
# Dislikes: 193
# Total Accepted:    269.6K
# Total Submissions: 562.6K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            list = [1 for _ in range(i+1)]
            if i>=2:
                for j in range(1,i):
                    list[j] = res[i-1][j]+res[i-1][j-1]
            res.append(list)
        return res[-1]

# @lc code=end

