'''
시간 복잡도: O(n)
- 리스트를 한 번 순회하면서 각 요소에 대해 최대값과 최소값을 갱신하므로 O(n)입니다.

공간 복잡도: O(1)
- 추가적인 배열을 사용하지 않고, 몇 개의 변수만 사용하므로 O(1)입니다.
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = nums[0]
        cur_max = nums[0]  # 현재 위치까지 최대 곱
        cur_min = nums[0]  # 현재 위치까지 최소 곱 (음수 대비)

        for i in range(1, n):
            temp_max = cur_max
            cur_max = max(nums[i], cur_max * nums[i], cur_min * nums[i])
            cur_min = min(nums[i], temp_max * nums[i], cur_min * nums[i])
            max_product = max(max_product, cur_max)

        return max_product
