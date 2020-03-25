#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (45.14%)
# Likes:    1469
# Dislikes: 56
# Total Accepted:    206.8K
# Total Submissions: 458.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.dfs(s,[],res)
        return res
         
    def isPalindrome(self,nums):
        return nums==nums[::-1]
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],path+[s[:i]],res)


        
# @lc code=end

