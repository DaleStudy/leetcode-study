# 시간복잡도: O(N)
# 공간복잡도: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for idx, num in enumerate(nums):
            check[num] = idx

        for idx, num in enumerate(nums):
            if num * 2 == target:
                if check[num] != idx:
                    return [idx, check[num]]
                else:
                    continue

            if target - num in check:
                return [check[num], check[target - num]]

        return []
