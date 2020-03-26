#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        max_len =start = 0
        for i,x in enumerate(s):
            if x in dict and start <= dict[x]:
                start = dict[x]+1
            else : max_len = max(max_len,i-start+1)
            dict[x] =i
        return max_len
# @lc code=end

