from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) >= 3 and set(nums) == set([0]):
            return [[0, 0, 0]]
        triplets = set()
        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                f = -(nums[i] + nums[j])
                if f in seen:
                    triplet = [nums[i], nums[j], f]
                    triplets.add(tuple(sorted(triplet)))
                seen.add(nums[j])
        return list(triplets)
