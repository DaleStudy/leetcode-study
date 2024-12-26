from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtract_map = {}

        for i, num in enumerate(nums):
            if num in subtract_map:
                return [i, subtract_map[num]]
            else:
                subtract_map[target - num] = i


# 시간 복잡도: O(n)
# - nums 배열을 한 번 순회하며 각 요소를 확인하므로 시간 복잡도는 O(n)입니다.
#
# 공간 복잡도: O(n)
# - 추가로 사용하는 subtract_map 딕셔너리에는 최악의 경우 nums 배열의 모든 요소가 저장되므로
#   공간 복잡도는 O(n)입니다.
