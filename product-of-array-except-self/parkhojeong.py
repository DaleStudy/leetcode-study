class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count >= 2:
            return [0] * len(nums)

        multiplied = 1
        for num in nums:
            if num == 0:
                continue
            multiplied = multiplied * num

        if zero_count == 1:
            return [multiplied if x == 0 else 0 for x in nums]

        return [int(multiplied / x) for x in nums]
