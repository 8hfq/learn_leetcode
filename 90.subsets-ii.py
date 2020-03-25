#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (45.17%)
# Likes:    1385
# Dislikes: 61
# Total Accepted:    254.8K
# Total Submissions: 559.9K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums,[],res)
        return res


    def dfs(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            if  i>0 and nums[i] == nums[i - 1]:
                continue
            # if i<len(nums)-1 and nums[i] == nums[i + 1]:
            #     continue
            self.dfs(nums[i+1:],path+[nums[i]],res)
        
# @lc code=end

