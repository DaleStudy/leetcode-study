# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
