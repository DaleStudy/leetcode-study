# 시간복잡도 : O(n)
# 공간복잡도 : O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {num: idx, ...}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i

        return []
   
