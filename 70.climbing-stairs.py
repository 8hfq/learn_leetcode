#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.09%)
# Likes:    3565
# Dislikes: 116
# Total Accepted:    595.5K
# Total Submissions: 1.3M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        s = [ 1 for i in range(n+1)]
        if n==1:
            return s[1]
        for i in range(2,n+1):
            s[i] = s[i-1]+s[i-2]
        return s[n]


# @lc code=end

