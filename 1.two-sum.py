#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i ,n in enumerate(nums):
            other = target-n
            if other in map:
                return [map[other],i]
            else:
                map[n] = i


        
# @lc code=end

