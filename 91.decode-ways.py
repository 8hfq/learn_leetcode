#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.60%)
# Likes:    2236
# Dislikes: 2471
# Total Accepted:    355.5K
# Total Submissions: 1.5M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        dp = [0 for i in range(len(s)+1)]
        dp[0:2] = [1,1]
        for i in range(2,len(s)+1):
            if  0<int(s[i-1])<=9:
                dp[i] =dp[i-1]
            if  10<=int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
        return dp[-1]
# @lc code=end

