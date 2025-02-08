"""
Solution: 
    1) 순회하며 이전 값이 현재 값보다 크거나 같다면 현재 값이 최소값이다.
    2) 끝까지 돌아도 최소값이 없을 경우 첫번쨰 값이 최소값이다.
Time: O(n)
Space: O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                return nums[i]

        return nums[0]

    """
    Solution: 
        시간 복잡도 O(log n)으로 풀기 위해 binary search 사용
    Time: O(log n)
    Space: O(1)
    """

    def findMin(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # prev 값보다 mid 가 작으면 찾던 값
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # mid 까지 정상 순서면 우측 탐색
            if nums[0] < nums[mid]:
                l = mid + 1
            # mid 까지 비 정상 순서면 좌측 탐색
            else:
                r = mid - 1
        # 못찾을 경우 전체 정상 순서 케이스
        return nums[0]
