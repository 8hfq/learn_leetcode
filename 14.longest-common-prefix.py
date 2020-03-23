#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i,j in enumerate(shortest):
            for others in strs:
                if others[i]!=j:
                    return shortest[:i]
        return shortest
        
        
        
# @lc code=end

