#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (35.94%)
# Likes:    1722
# Dislikes: 69
# Total Accepted:    192.9K
# Total Submissions: 531.7K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices) :
        first = [0 for i in range(len(prices))]
        second = [0 for i in range(len(prices))]
        prices1=[]+prices
       
        
        for i in range(1,len(prices)):
            first[i] = max(first[i-1],prices1[i]-prices1[i-1])
            prices1[i] = min(prices1[i],prices1[i-1])
            
        prices2=[]+prices
        for j in range(len(prices)-2,-1,-1):
            second[j] = max(second[j+1],(prices2[j+1]-prices2[j]))
            prices2[j] = max(prices2[j],prices2[j+1])   

        res = 0
        for i in range(len(first)):
            res = max(res,first[i]+second[i])
        return res
# @lc code=end

