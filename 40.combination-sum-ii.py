#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        self.dfs(candidates,target,0,[],result)
        return result
        

    def dfs(self, nums,target,index,path,result):
        if target<0:
            return
        if target==0:
            result.append(path)
            return
        
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i - 1]:
             continue
            if nums[i] > target:
                break
            self.dfs(nums,target-nums[i],i+1,path+[nums[i]],result)

# @lc code=end

