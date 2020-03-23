
if __name__ == "__main__":
    nums=[1,2,3,4,5,6,7,8,9]
    target=9
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
        print(left,mid,right)