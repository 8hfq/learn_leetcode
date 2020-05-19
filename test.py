class Solution:
    def singleNumber(self, nums) -> int:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0)+1
        for k,v in dict.items:
            if v==1:
                return k



if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))