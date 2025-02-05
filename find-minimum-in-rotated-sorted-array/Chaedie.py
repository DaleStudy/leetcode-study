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
