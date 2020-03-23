#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for i in matrix:
                    res.append(i.pop())
            if matrix:
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    res.append(i.pop(0))
        return res
# @lc code=end

