#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (20.39%)
# Likes:    1517
# Dislikes: 222
# Total Accepted:    164.6K
# Total Submissions: 794.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
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
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
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
# Output: []
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
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        self.dfs(beginWord,endWord,wordList,[beginWord],res)
        if not res:
            return []
        minlen = len(min(res,key=len))
        result = []
        for  x in res:
            if len(x) ==minlen:
                result.append(x)
        return result

    def isOnlyOneChange(self,a,b):
        n = len(a)
        j =0
        for i in range(n):
            if a[i]!=b[i]:
                j+=1
        return j==1
    
    def dfs(self,word,endWord,wordList,path,res):
        if res and len(path) > len(min(res)):
            return
        if word ==endWord:
            res.append(path)
        if not wordList:
            return
        
        for i,x in enumerate(wordList):
            if self.isOnlyOneChange(word,x):
                self.dfs(x,endWord,wordList[:i]+wordList[i+1:],path+[x],res)



# @lc code=end

