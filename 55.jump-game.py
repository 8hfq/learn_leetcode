#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach, n = 0,len(nums)
        for i ,x in enumerate(nums):
            if max_reach<i: return False
            if max_reach>=n-1: return True
            max_reach = max(max_reach,i+x)
        
# @lc code=end

