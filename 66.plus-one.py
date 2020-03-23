#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        j =1
        for i,x in enumerate(digits):
            x=x+j
            if x==10:
                digits[i] =0
                j=1 
            else: 
                digits[i] = x
                j=0
            if j==0:
                return digits[::-1]
        if j==1:
            digits.append(1)
        return digits[::-1]
        
# @lc code=end

