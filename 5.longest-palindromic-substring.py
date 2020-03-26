#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len  =''
        start =end =0 
        for i in range(len(s)):
            len1 = self.getPalindrome(s,i,i)
            len2 = self.getPalindrome(s,i,i+1)
            if len(len1)>len(max_len):
                max_len = len1
            if len(len2) > len(max_len):
                max_len = len2
        return max_len


        
    def getPalindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1 
        return s[l+1:r]

# @lc code=end

