#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (32.82%)
# Likes:    1501
# Dislikes: 698
# Total Accepted:    264.5K
# Total Submissions: 805.9K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =='0' or num2=='0':
            return '0'
        result = self.cf(num1[-1],num2)
        j=0
        for i in num1[::-1]:
            if j>0:
                r = self.cf(i,num2)+'0'*j 
                result = str(int(result)+int(r))
            j+=1
        return result


        
  
    


    def cf(self,one,list):
        res = ''
        tmp = 0
        for i in list[::-1]:
            r = int(one) * int(i) +tmp
            if r>9:
                res = str(r)[1:]+res
                tmp = int( str(r)[:1])
            else: 
                res = str(r)+res 
                tmp=0
        if tmp!=0:
            res = str(tmp)+res
        return res

        
# @lc code=end

