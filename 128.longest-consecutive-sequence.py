#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (43.76%)
# Likes:    2750
# Dislikes: 160
# Total Accepted:    270.9K
# Total Submissions: 615K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        map = {}
        for n in nums:
            if not n in map:
                left =map.get(n-1) if (n-1) in map else 0
                right =map.get(n+1) if (n+1) in map else 0
                sum = left+right+1
                map[n] = sum
                res = max(res,sum)
                map[n-left] = sum
                map[n+right] = sum
        return res
# @lc code=end

