class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(N) Time complexity
        """
        N = len(nums)

        zeroes = nums.count(0)

        if zeroes > 1:
            return [0] * N

        ans = [0] * N
        acc = 1

        # This could make logic complex, so treat it separately
        if zeroes == 1:
            place = nums.index(0)
            for i in range(N):
                if i != place:
                    acc *= nums[i]
            ans[place] = acc
            return ans

        for i in range(N):
            ans[i] = acc
            acc *= nums[i]

        acc = 1

        for i in range(N - 1, -1, -1):
            ans[i] *= acc
            acc *= nums[i]

        return ans
