'''
# 33. Search in Rotated Sorted Array

binary search + condition check

이진 탐색 중, 왼쪽이 정렬되었을 때
- 타겟이 정렬된 왼쪽에 있는 경우, 왼쪽 탐색 (left부터 mid - 1 사이에서 타겟을 탐색)
- 타겟이 정렬된 왼쪽에 없을 경우, 오른쪽 탐색 (mid + 1부터 right 사이에서 타겟을 탐색)

이진 탐색 중, 오른쪽이 정렬되었을 때
- 타겟이 정렬된 오른쪽에 있는 경우, 오른쪽 탐색 (mid + 1부터 right 사이에서 타겟을 탐색)
- 타겟이 정렬된 오른쪽에 없을 경우, 왼쪽 탐색 (left부터 mid - 1 사이에서 타겟을 탐색)

## TC: O(log n)

binary search

## SC: O(1)

no extra space

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # is_left_sorted
                if nums[left] <= target < nums[mid]: # is_target_left
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: # is_target_right
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
