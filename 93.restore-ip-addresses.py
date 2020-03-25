#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (33.62%)
# Likes:    999
# Dislikes: 453
# Total Accepted:    174K
# Total Submissions: 512.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        list = [1,2,3]
        res =[]
        result = []
        self.dfs(s,[],res,list)
        if not res:
            return res
        for ip in res:
            for j in range(1,4):
                ip[0]+= '.'+ip[j]
            result.append(ip[0])
        return result
    
    def isIp(self,nums):
        if  int(nums)>255:
            return False
        elif len(nums)>1 and nums[0]=='0':
            return False
        else :return True
        
    def dfs(self,nums,path,res,list):
        if len(path) >4:
            return
        if not nums and len(path)==4:
            res.append(path)
        for i in list:
            if i <=len(nums):
                if self.isIp(nums[:i]):
                    self.dfs(nums[i:],path+[nums[:i]],res,list)


# @lc code=end

