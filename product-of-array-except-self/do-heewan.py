class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        x = 1
        for element in nums:
            result.append(x)
            x *= element

        x = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= x
            x *= nums[i]

        return result

