#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (27.46%)
# Likes:    2581
# Dislikes: 1031
# Total Accepted:    376.2K
# Total Submissions: 1.3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: 0
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        res = []
        self.dfs(beginWord,endWord,wordList,1,res)
        if not res:
            return 0
        return min(res)
    def isOnlyOneChange(self,a,b):
        n = len(a)
        j =0
        for i in range(n):
            if a[i]!=b[i]:
                j+=1
        return j==1
    def dfs(self,word,endWord,list,index,res):
        if res and index>= min(res):
            return
        if word ==endWord:
            res.append(index)
            return
        if not list:
            return
        for i,x in enumerate(list):
            if self.isOnlyOneChange(word,x):
                self.dfs(x,endWord,list[:i]+list[i+1:],index+1,res)
        
# @lc code=end

