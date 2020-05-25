#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = [int(v) for v in version1.split('.')]
        list2 = [int(v) for v in version2.split('.')]
        maxlen = max(len(list1), len(list2))
        for i in range(maxlen):
            v1 = list1[i] if i <len(list1) else 0
            v2 = list2[i] if i< len(list2) else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0
# @lc code=end

