#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        end = 0 
        maxPosition =0
        for i in range(len(nums)-1):
            maxPosition = max(maxPosition,nums[i]+i)
            if i==end:
                end = maxPosition
                step+=1 
            if end ==len(nums)-1:
                return step
        return step

# @lc code=end

