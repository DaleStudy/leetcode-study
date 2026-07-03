class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(N) Time complexity
        """
        N = len(nums)

        ans = [0] * N

        acc = 1

        for i in range(N):
            ans[i] = acc
            acc *= nums[i]

        acc = 1

        for i in range(N - 1, -1, -1):
            ans[i] *= acc
            acc *= nums[i]

        return ans
