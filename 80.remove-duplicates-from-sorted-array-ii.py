#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i =0 
        for j in nums:
            if i<2 or nums[i-2]!=j:
                nums[i] = j
                i+=1
        return i

# @lc code=end

