#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]
        n = len(height)-1
        left_max[0] = height[0]
        ase =0
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1],height[i])
            i+=1 
        right_max[n] = height[n]
        for i in range(n-1,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
            i-=1 
        for i in range(1,n):
            ase += min(left_max[i],right_max[i])-height[i]
        return ase

        
# @lc code=end

