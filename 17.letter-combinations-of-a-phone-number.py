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
        result = []
        if not digits:
            return result
        self.backtrack('',digits,result,phone)
        return result


    def backtrack(self,path,digits,result,phone):
        if not digits:
            result.append(path)
        else:
            for i in phone[digits[0]]:
                self.backtrack(path+i,digits[1:],result,phone)
            
# @lc code=end

