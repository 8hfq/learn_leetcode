#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.gennrate(n,n,"",res)
        return res

    def gennrate(self,left,right,str,res):
        if left==0 and right==0:
            res.append(str)
            return
        if left >0 :
            self.gennrate(left-1,right,str+"(",res)
        if right>left:
            self.gennrate(left,right-1,str+")",res)
# @lc code=end

