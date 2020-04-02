class Solution:
    def maxProfit(self, prices) :
        first = [0 for i in range(len(prices))]
        second = [0 for i in range(len(prices))]
        prices1=[]+prices
       
        
        for i in range(1,len(prices)):
            first[i] = max(first[i-1],prices1[i]-prices1[i-1])
            prices1[i] = min(prices1[i],prices1[i-1])
            
        
        print(first)
        prices2=[]+prices
        for j in range(len(prices)-2,-1,-1):
            second[j] = max(second[j+1],(prices2[j+1]-prices2[j]))
            prices2[j] = max(prices2[j],prices2[j+1])   
        print(second) 
        res = 0
        for i in range(len(first)):
            res = max(res,first[i]+second[i])
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([6,1,3,2,4,7]))
 