// TC: O(n)
// SC: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_unique = set(nums)

        ans = 0

        for num in nums_unique:
            if (num - 1) in nums_unique:
                continue

            next = num + 1

            while next in nums_unique:
                next = next + 1

            ans = max(ans, next - num)

        return ans

