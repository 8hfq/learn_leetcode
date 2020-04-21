#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.69%)
# Likes:    4788
# Dislikes: 180
# Total Accepted:    647.1K
# Total Submissions: 1.4M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nx = len(grid)
        res = 0
        if nx==0:
            return res
        ny = len(grid[0])
        for x in range(nx):
            for y in range(ny):
                if grid[x][y]=='1':
                    res+=1
                    self.dfs(grid,x,y)
        return res
        

    def dfs(self,grid,x,y):
        grid[x][y]=0
        nx = len(grid)
        ny = len(grid[0])
        for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=a<nx and 0<=b<ny and grid[a][b]=='1':
                self.dfs(grid,a,b)

# @lc code=end

