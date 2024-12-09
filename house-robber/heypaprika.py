class Solution:
    def rob(self, nums: List[int]) -> int:
        a = [0] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
            
        a[0] = nums[0]
        a[1] = nums[1]
        a[2] = max(a[0] + nums[2], a[1])

        for i in range(3, len(nums)):
            a[i] = max(a[i-3], a[i-2]) + nums[i]

        return max(a)

