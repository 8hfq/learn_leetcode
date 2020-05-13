#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while len(stack)>1 and heights[i]<=heights[stack[-1]]:
                res = max(res,heights[stack.pop()]* (i-1-stack[-1]))
            stack.append(i)
        for i in range(len(stack)-1):
            res = max(res,heights[stack.pop()]*(len(heights)-stack[-1]-1))
        return res 
# @lc code=end

