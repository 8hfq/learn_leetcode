#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def backtrack(combinations,next_digits):
            if len(next_digits)==0:
                result.append(combinations)
            else: 
                for i in phone[next_digits[0]]:
                    backtrack(combinations+i,next_digits[1:])
        result=[]
        if digits:
            backtrack("",digits)
        return result
        
# @lc code=end

