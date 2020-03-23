#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (60.74%)
# Likes:    3198
# Dislikes: 95
# Total Accepted:    531.6K
# Total Submissions: 875.3K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums,[],res)
        return res

    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
# @lc code=end

