"""
Solution: 1) DFS Brute Force -> TLE
Time: O(2^n * nlogn)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        sub = []
        max_len = 0

        def dfs(i, length):
            nonlocal max_len
            if i == len(nums):
                if sub == sorted(list(set(sub))):
                    max_len = max(len(sub), max_len)
                return

            dfs(i + 1, length)
            sub.append(nums[i])
            dfs(i + 1, length)
            sub.pop()

        dfs(0, 0)
        return max_len


"""
풀이를 보고 적었으며, 완벽히 이해 되지는 않습니다.
Time: O(n^2)
Space: O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
