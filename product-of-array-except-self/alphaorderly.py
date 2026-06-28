class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(N) Time complexity
        O(N) Space complexity

        If output array does not count as extra space as written in follow up,
        it is O(1) solution
        """
        N = len(nums)

        z_count = 0
        multed = 1

        # 1. Create a multiplied number contains all array integers
        # - Count zero for edge case
        for n in nums:
            if n == 0:
                z_count += 1
                if z_count > 1:
                    return [0] * N
                continue

            multed *= n

        ans = [0] * N

        # 2. Generate ans array with edge case ( 1 zero number )
        for i, n in enumerate(nums):
            if z_count == 1:
                if n == 0:
                    ans[i] = multed
                continue

            ans[i] = multed // n

        return ans
