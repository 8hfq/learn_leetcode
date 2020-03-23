#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[1 for i in range(n)] for i in range(m)]
        for i in range(1,m): 
            for j in range(1,n):
                map[i][j] = map[i-1][j] + map[i][j-1]
        return map[-1][-1]
        
# @lc code=end

