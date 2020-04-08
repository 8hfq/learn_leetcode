
class Solution:
    def maxProduct(self, nums):
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        print(A)
        print(B)
        return max(A+B)
if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
 