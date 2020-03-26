#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
   
    def romanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        res, p = 0, 'I'
        for c in s[::-1]:
            if d[c] <d[p]:
                res =  res-d[c]
            else: res =res+d[c]
            p = c
        
        return res
# @lc code=end

