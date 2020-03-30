#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.45%)
# Likes:    555
# Dislikes: 2179
# Total Accepted:    344.1K
# Total Submissions: 1.1M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a maximal substring consisting of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s =="":
            return 0
        s = s[::-1]
        j=0
        for i in range(len(s)):
            if i==0 and s[i]==' ':
                j+=1
            else: 
                if s[i]==' ' and s[i-1]==' ':
                    j+=1
                if s[i]==' ' and s[i-1]!=' ':
                    return i-j
        return len(s)-j
# @lc code=end

