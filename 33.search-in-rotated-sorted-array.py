#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0,len(nums) - 1
   
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[r]:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else :l = mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else: r = mid-1
        return -1


        
# @lc code=end

