# Approach : De-duplicate using Set
# Complexity: O(n)
# Space complexity: O(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dedup = set(nums)
        return len(dedup) != len(nums)
