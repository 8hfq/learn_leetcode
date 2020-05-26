#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (34.88%)
# Likes:    770
# Dislikes: 171
# Total Accepted:    85.6K
# Total Submissions: 245.3K
# Testcase Example:  '[3,6,9,1]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
# 
# Return 0 if the array contains less than 2 elements.
# 
# Example 1:
# 
# 
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
# (3,6) or (6,9) has the maximum difference 3.
# 
# Example 2:
# 
# 
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# 
# Note:
# 
# 
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# Try to solve it in linear time/space.
# 
# 
#

# @lc code=start
import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length<=1:
            return 0
        min_nums = min(nums)
        max_nums = max(nums)
        if max_nums-min_nums==0:
            return 0 
        interval = math.ceil((max_nums-min_nums)/(length-1))
        bucketMin = [-1 for i in range(length-1)]
        bucketMax = [math.inf for i in range(length-1)]
        for i in range(length):
            index = math.ceil((nums[i] -min_nums )/interval)
            if nums[i] == min_nums or nums[i]==max_nums:
                continue
            bucketMin[index] = min(nums[i],bucketMin[index])
            bucketMax[index] = max(nums[i],bucketMax[index])

        maxGap = 0
        previousMax = min_nums
        for i in range(length-1):
            if bucketMax[i]==math.inf:
                continue
            maxGap = max(bucketMin[i]-previousMax,maxGap)
            previousMax = bucketMax[i]

        maxGap = max(max_nums-previousMax,maxGap)
        return maxGap
# @lc code=end

