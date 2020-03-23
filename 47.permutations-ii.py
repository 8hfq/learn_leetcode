#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (44.51%)
# Likes:    1620
# Dislikes: 57
# Total Accepted:    318.4K
# Total Submissions: 715.2K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        self.dfs(nums,[],res)
        return res

    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                if i>0:
                    if nums[i] ==nums[i-1]:
                        continue
                self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
        
# @lc code=end

