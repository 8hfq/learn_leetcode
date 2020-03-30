#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (42.17%)
# Likes:    1478
# Dislikes: 255
# Total Accepted:    401.5K
# Total Submissions: 942.1K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        tmp =0
        a = list(a)
        b = list(b)
        while a or b or tmp:
            if a: 
                tmp+= int(a.pop())
            if b:
                tmp+= int(b.pop())
            result +=str(tmp%2)
            tmp //=2
        return result[::-1]
# @lc code=end

