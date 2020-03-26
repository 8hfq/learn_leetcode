class Solution:
    def countAndSay(self, n: int) -> str:
        nums = ['1' for i in range(n)]
        if n==1:
            return nums[-1]
        for i in range(1,n):
            res=''
            count =1
            after = nums[i-1]
            for j in range(len(after)): 
                if j==len(after)-1 or after[j] !=after[j+1]:
                    res+=str(count)
                    res+=after[j]
                else : count+=1
            nums[i] = res 
            count =1
        return nums[-1]
                
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(5)
 