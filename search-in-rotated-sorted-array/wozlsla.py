"""
# Intuition

possibly left rotated at an unknown index k → 회전된 배열, 이 조건이 있는 이유?

시간 복잡도 O(logn)
  → 데이터의 크기가 커질수록 처리 시간이 매우 느리게 증가 - 탐색에 자주 사용됨
  → 어떤 알고리즘을 사용해야 하는가?

회전으로 인해 배열 전체가 정렬되어 있지 않지만(두개의 정렬된 배열), O(logn)의 성능을 유지하면서 target을 찾으려면?


# Approach

*회전된 배열 → 중앙값을 기준으로 배열을 나눴을 때, 최소한 한쪽 절반은 정렬되어 있음.
*(예시에서) nums[low](4) < nums[mid](7) 이므로 왼쪽 부분배열은 정렬되어 있음.

N → N/2
1. 어느 쪽이 정렬되어 있는가?
2. target이 그 안에 포함되는가?
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            # mid = low + (high - low) // 2
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽이 정렬된 경우
            if nums[low] <= nums[mid]:

                # target 확인
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # 오른쪽이 정렬된 경우 (nums[mid] < nums[high])
            else:

                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
