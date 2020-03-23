#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x[0])
        n = len(intervals)
        result=[]
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

