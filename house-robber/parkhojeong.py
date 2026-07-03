class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        arr = [0] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if i >= 3:
                candidate1 = arr[i - 2] + num
                candidate2 = arr[i - 3] + num
                arr[i] = max(candidate1, candidate2)
            elif i == 2:
                arr[i] = arr[i - 2] + num
            else:
                arr[i] = num

        return max(arr[-1], arr[-2])
