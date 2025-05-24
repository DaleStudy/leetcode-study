# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            양끝에서부터 범위를 좁히면서 확인하는 two-pointer를 이용한다.
            양끝 side 중 더 작은 쪽을 안쪽으로 한 칸 옮기면서 확인하고,
            만약 두 side가 길이가 같다면 두 개를 모두 안쪽으로 한 칸 옮긴다.
        """

        lo, hi = 0, len(height) - 1
        max_amount = 0

        while lo < hi:
            # 양 끝 side 길이
            s1, s2 = height[lo], height[hi]

            # max_amount 업데이트
            max_amount = max(max_amount, (hi - lo) * min(s1, s2))

            # 더 낮은 side를 안쪽으로 한 칸 옮기기
            if s1 < s2:
                lo += 1
            elif s1 > s2:
                hi -= 1
            # 두 side의 크기가 같다면, 둘다 안쪽으로 한 칸씩 옮기기
            else:
                lo += 1
                hi -= 1

        return max_amount
