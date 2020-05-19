#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (29.17%)
# Likes:    882
# Dislikes: 29
# Total Accepted:    122.7K
# Total Submissions: 416.5K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        if self.isPalindrome(s):
            return 0
        res = []
        self.dfs(s,0,res)
        return min(res)
        

    def isPalindrome(self,nums):
        return nums==nums[::-1]
    def dfs(self,s,index,res):
        if res and index>=min(res):
            return
        if self.isPalindrome(s):
            res.append(index)
            return
        for i in range(len(s),0,-1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],index+1,res)
        
# @lc code=end

