from collections import *
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res =''
        left, cnt, minLen = 0, 0, float('inf')
        c  =Counter(t)
        for  i in range(len(s)):
            c[s[i]]-=1
            if c[s[i]]>=0:
                cnt +=1
            while cnt ==len(t):
                if minLen >= i -left+1:
                    minLen =i-left+1
                    res = s[left:i+1]
                if c[s[left]] >=0:
                    cnt-=1
                c[s[left]]+=1
                left+=1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC",  "ABC"))
 