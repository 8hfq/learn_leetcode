#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (51.92%)
# Likes:    1207
# Dislikes: 61
# Total Accepted:    262.6K
# Total Submissions: 500.9K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        path = []
        res = []
        self.dfs(nums,k,path,res)
        return res
        
    def dfs(self,nums,k,path,res):
        if k==0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i+1:],k-1,path+[nums[i]],res)
# @lc code=end

