class Solution:
    def candy(self, ratings):
        n = len(ratings)
        left = [1 for i in range(n)] 
        right = [1 for i in range(n)]
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1 
        for j in range(n-2,-1,-1):
            print(right[j])
            if ratings[j]>ratings[j+1]:
                right[j] = right[j+1]+1 
        res = 0 
        for i in range(n):
            res +=max(left[i],right[i])
        return res      
if __name__ == "__main__":
    s = Solution()
    print(s.candy([1,0,2]))
 