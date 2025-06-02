from typing import List

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/

문제: 회전된 오름차순 정렬된 배열 nums에서 target 값의 인덱스를 반환하라.

Idea: 이진 탐색 패턴 사용

TC: O(logN)
SC: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽이 정렬된 경우
            if nums[left] <= nums[mid]:
                # target이 정해진 구간에 있는 경우
                if nums[left] <= target < nums[mid]:
                    # 왼쪽만 탐색하도록 right를 줄임
                    right = mid - 1
                # 아니라면 오른쪽으로 범위를 옮김
                else:
                    left = mid + 1
            # 오른쪽이 정렬된 경우
            else:
                # target이 정해진 구간에 있는 경우
                if nums[mid] < target <= nums[right]:
                    # 오른쪽만 탐색하도록 left를 늘림
                    left = mid + 1
                # 아니라면 왼쪽으로 범위를 옮김
                else:
                    right = mid - 1
        return -1
