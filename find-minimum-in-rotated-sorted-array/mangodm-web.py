from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - Idea: 회전된 정렬 배열에서 가장 작은 값을 찾기 위해 두 개의 포인터, left, right를 이용한다.
            두 개의 포인터는 조건에 따라 배열에서 탐색할 범위를 줄여가는데 활용된다.
        - Time Complexity: O(logn). n은 배열의 크기이다.
            매번 배열을 절반으로 나눠서 탐색 범위를 줄이기 때문에 O(logn) 시간이 걸린다.
        - Space Complexity: O(1). 배열의 크기와 상관없이 left, right, mid 변수만 사용되므로
            상수 공간만 차지한다.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
