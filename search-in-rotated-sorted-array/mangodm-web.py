from typing import List


class Solution:
    """
    - 아이디어: 배열의 중간 값을 기준으로 왼쪽, 오른쪽 중 한쪽은 항상 정렬되어 있다.
        이 특징에 착안하여, 어느 쪽이 먼저 정렬되어 있는지 확인하고, 그 안에
        찾으려는 값이 있는지를 확인하는 방식으로 탐색 범위를 좁혀간다.
    - 시간 복잡도: O(logn). n은 배열의 길이.
      배열을 절반씩 나누어 탐색을 진행하기 때문에 시간 복잡도는 O(logn)이다.
    - 공간 복잡도: O(1). 추가적인 메모리를 사용하지 않고, 상수 공간만 필요하다.
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
