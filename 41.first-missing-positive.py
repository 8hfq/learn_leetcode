#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # print nums[i], i + 1, nums[nums[i] - 1]
            while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print nums
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1
# @lc code=end

