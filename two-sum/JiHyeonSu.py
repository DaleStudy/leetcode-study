# 해시맵을 활용한 두 수의 합 구현
# 시간복잡도 및 공간복잡도 O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in n_map:
                return [n_map[diff], i]
            n_map[num] = i
