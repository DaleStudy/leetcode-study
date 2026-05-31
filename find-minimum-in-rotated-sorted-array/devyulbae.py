"""
Blind 75 - Find Minimum in Rotated Sorted Array
LeetCode Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
시간복잡도 : O(log n)
공간복잡도 : O(1)
풀이 : 이진 탐색
중간점 기준으로 nums[mid-1] > nums[mid] 이면 mid가 최소값
그렇지 않으면 왼쪽 절반이 정렬되어 있는지 확인해서 왼쪽 절반 or 오른쪽 절반으로 탐색 범위를 좁혀나감
만약 발견되지 않았다면 nums[0]이 최소값
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid -1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0]

