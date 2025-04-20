# 투포인터를 활용해보기

def threeSum(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    result = set()
    for i in range(n):
        l,r = i+1,n-1
        while l<r:
            res = nums[i] + nums[l] + nums[r]
            if res < 0:
                l += 1
            elif res > 0:
                r -= 1
            else:
                result.add((nums[i], nums[l], nums[r]))
                l += 1
    return list(result)

