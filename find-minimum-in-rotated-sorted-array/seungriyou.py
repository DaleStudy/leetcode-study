# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(logn)
            - SC: O(1)

        [Approach]
            기본적으로 rotated sorted array에서 O(logn) time에 minimum element를 찾아야하므로
            binary search를 사용한다. 규칙을 찾아보면 다음과 같다.
                - nums[mid] > nums[hi]: min element가 오른쪽 영역인 (mid, hi]에 있음
                - nums[mid] < nums[hi]: min element가 왼쪽 영역인 [lo, mid]에 있음
        """

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1  # (mid, hi]에 min element 존재
            else:
                hi = mid  # [lo, mid]에 min element 존재

        return nums[lo]
