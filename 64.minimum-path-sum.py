#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i<1 and j>0: 
                    grid[i][j] += grid[i][j-1]
                if j<1 and i>0: 
                    grid[i][j] +=grid[i-1][j]
                if i>=1 and j>=1:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
# @lc code=end

