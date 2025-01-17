# 시간복잡도: O(n)
# 공간복잡도: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = [1] * len(nums)

        for idx in range(len(nums)):
            if idx == 0:
                prefix[idx] = nums[idx]
            else:
                prefix[idx] = prefix[idx - 1] * nums[idx]
        
        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                suffix[idx] = nums[idx]
            else:
                suffix[idx] = suffix[idx + 1] * nums[idx]

        for idx in range(len(nums)):
            if idx == 0:
                product[idx] = suffix[idx + 1]
            elif idx == len(nums) - 1:
                product[idx] = prefix[idx - 1]
            else:
                product[idx] = prefix[idx - 1] * suffix[idx + 1]

        return product

