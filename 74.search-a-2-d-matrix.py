#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.84%)
# Likes:    1404
# Dislikes: 145
# Total Accepted:    293.7K
# Total Submissions: 816.8K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        # while row < len(matrix) and col >= 0:
        #     if matrix[row][col] == target: return True
        #     elif matrix[row][col] < target: row += 1
        #     elif matrix[row][col] > target: col -= 1

        # return False
        while row< len(matrix) and col>=0:
            if matrix[row][col] ==target:
                return True 
            elif matrix[row][col] <target :
                row+=1
            elif matrix[row][col] >target:
                col-=1
        return False

# @lc code=end

