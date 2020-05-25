#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i,x in enumerate(numbers):
            if x in dict.keys():
                return [dict[x]+1,i+1]
            two_target = target-x
            dict[two_target] = i


            
# @lc code=end

