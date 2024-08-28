from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        if len(nums) == k:
            return list(set(nums))

        num_cnt = defaultdict(int)
        for num in nums:
            num_cnt[num] += 1

        return list(
            sorted(
                num_cnt, 
                key=lambda x: num_cnt[x], 
                reverse=True
            )
        )[:k]
