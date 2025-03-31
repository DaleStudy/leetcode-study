'''
시간 복잡도: O(log n)
- 이진 탐색(Binary Search)을 사용하여 배열을 절반씩 나누며 탐색하므로 O(log n)입니다.

공간 복잡도: O(1)
- 추가적인 배열을 사용하지 않고, 몇 개의 변수만 사용하므로 O(1)입니다.
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 절반이 정렬되어 있는 경우
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:    # 타겟이 왼쪽 범위 내에 있음
                    right = mid - 1
                else:                                   # 타겟이 오른쪽 범위에 있음
                    left = mid + 1
            # 오른쪽 절반이 정렬된 경우
            else:
                if nums[mid] < target <= nums[right]:   # 타겟이 오른쪽 범위 내에 있음
                    left = mid + 1
                else:                                   # 타겟이 왼쪽 범위에 있음
                    right = mid - 1

        return -1
