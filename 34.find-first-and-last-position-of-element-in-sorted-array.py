#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l ,r = 0,len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid]>target:
                r= mid-1
            if nums[mid]<target:
                l = mid+1
            if nums[mid]==target:
                i=j=mid
                while i<r and nums[i+1] ==target :
                    i+=1     
                while j>l and nums[j-1] ==target:
                    j-=1
                return [j,i]
        return [-1,-1]

        
# @lc code=end

