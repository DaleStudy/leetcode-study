from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        - Idea: 배열의 양쪽 끝에서 시작하는 두 포인터(left, right)를 이용해 두 선 사이의 최대 영역을 구한다. 둘 중, 높이가 낮은 쪽의 포인터는 중앙 쪽으로 이동시킨다.
        - Time Complexity: O(n), n은 주어진 배열(height)의 길이.
        - Space Complexity: O(1), 추가 공간은 사용하지 않는다.
        """
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            result = max(result, current_width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
