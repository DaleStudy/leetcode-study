'''
시간 복잡도: O(n)
- 두 포인터를 이동하면서 배열을 한 번만 순회하므로 시간 복잡도는 O(n)입니다.

공간 복잡도: O(1)
- 추가 메모리를 사용하지 않고 변수만 사용하므로 O(1)입니다.
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
