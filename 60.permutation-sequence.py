#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (35.43%)
# Likes:    1220
# Dislikes: 290
# Total Accepted:    167K
# Total Submissions: 471.2K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]*(n+1)
        for i in range(1, n+1):
            factorials[i] = factorials[i-1]*i
            
        n_list = [i for i in range(1, n+1)]

        k -= 1
        res = ''
        for i in range(1, n+1):
            m = k // factorials[n-i]
            k =k% factorials[n-i]     
            res += str(n_list[m])
            n_list.remove(n_list[m])

        return res

# @lc code=end

