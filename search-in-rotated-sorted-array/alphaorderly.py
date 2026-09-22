"""
시간복잡도: O(log n)
공간복잡도: O(1)

- 회전된 정렬 배열에서 이진 탐색으로 target을 찾는다.
- mid와 target이 원래 배열의 왼쪽 절반에 있었는지, 오른쪽 절반에 있었는지를 구분한다.
    - 기준: nums[mid] > nums[N-1] 이면 mid가 왼쪽(회전되기 전 더 작은 쪽), 아니면 오른쪽.
    - target도 같은 기준으로 왼쪽/오른쪽인지 판별.
- mid와 target이 서로 다른 쪽에 있으면, target이 있는 쪽으로 포인터를 이동 (left 또는 right 값을 조정).
- mid == target 이면 mid 반환.
- 찾지 못하면 -1 반환.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left = 0
        right = N - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            mid_left = nums[mid] > nums[N - 1]
            target_left = target > nums[N - 1]

            if nums[mid] > target:
                if mid_left != target_left:
                    left = mid + 1
                else:
                    right = mid - 1
            elif mid_left != target_left:
                right = mid - 1
            else:
                left = mid + 1

        return -1
