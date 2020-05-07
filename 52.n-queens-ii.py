#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        self.dfs([-1]*n,0,res)
        return len(res)
        

    def dfs(self,nums,index,res):
        if len(nums) ==index:
            res.append([0])
            return 
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums,index):
                self.dfs(nums,index+1,res)
    def valid(self,nums,n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i]==nums[n]:
                return False
        return True

# @lc code=end

