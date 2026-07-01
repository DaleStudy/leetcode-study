# TC: O(N)
# SC: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_prod = [0] * n
        suffix_prod = [0] * n

        prefix_prod[0] = nums[0]
        suffix_prod[-1] = nums[-1]

        for idx in range(1, n):
            prefix_prod[idx] = prefix_prod[idx - 1] * nums[idx]
            suffix_prod[-idx - 1] = suffix_prod[-idx] * nums[-idx - 1]

        ret = []

        ret.append(suffix_prod[1])
        for idx in range(1, n - 1):
            ret.append(prefix_prod[idx - 1] * suffix_prod[idx + 1])
        ret.append(prefix_prod[n - 2])

        return ret

