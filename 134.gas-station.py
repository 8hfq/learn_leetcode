#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        now = 0
        index = 0
        for i in range(len(gas)): 
            total +=gas[i] -cost[i]
            now += gas[i] -cost[i]
            if now <0: 
                index = i+1 
                now = 0
        return index if total>=0 else -1
# @lc code=end

