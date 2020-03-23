#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals = sorted(intervals, key = lambda x: x[0])
        n = len(intervals)
        if n<2: return intervals
        for i in range(n-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i+1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        result.append(intervals[n-1])
        return result

        
# @lc code=end

