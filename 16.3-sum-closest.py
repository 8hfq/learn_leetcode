#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            n=i+1
            m = len(nums)-1
            while n<m:
                sum = nums[i]+nums[n]+nums[m]
                if sum ==target:
                    return sum
                elif abs(result-target) > abs(sum-target):
                    result = sum
                if sum-target<0:
                        n+=1
                else : m-=1
        return result

        
# @lc code=end

