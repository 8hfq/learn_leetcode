#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N ,result = len(nums) ,[]
        for i in range(N):
            if i >0 and nums[i]==nums[i-1]:
                continue
            target = nums[i]*-1
            m ,n = i+1,N-1
            while m<n:
                if nums[m]+nums[n]==target:
                    result.append([nums[i],nums[m],nums[n]])
                    m =m+1
                    while m<n and nums[m]==nums[m-1]:
                        m= m+1
                elif nums[m]+nums[n]>target:
                    n = n-1
                elif nums[m]+nums[n]<target:
                    m = m+1
        return result




        
# @lc code=end

