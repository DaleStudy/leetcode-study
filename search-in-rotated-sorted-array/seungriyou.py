# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search_1(self, nums: List[int], target: int) -> int:
        """
        [Complexity]
            - TC: O(logn)
            - SC: O(1)

        [Approach]
            sorted array를 다루면서 O(log n) time에 수행되어야 하므로 binary search를 사용해야 한다.
            기본적으로 sorted array이므로, rotated 되었더라도 mid를 기준으로 한 쪽은 무조건 sorted이다.
            그리고 sorted인 부분에 target이 존재하는지 여부는 양끝 값과만 비교하더라도 알 수 있다.
            따라서 다음의 두 가지 경우로 나누어 볼 수 있다.
                1) 왼쪽이 sorted
                    -> target이 왼쪽에 포함되면 왼쪽으로, 아니라면 오른쪽으로
                2) 오른쪽이 sorted
                    -> target이 오른쪽에 포함되면 오른쪽으로, 아니라면 왼쪽으로
        """
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            # 1) 왼쪽이 sorted
            if nums[lo] <= nums[mid]:
                # target이 왼쪽에 포함되면 왼쪽 살펴보기
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                # 아니라면 오른쪽 살펴보기
                else:
                    lo = mid + 1
            # 2) 오른쪽이 sorted
            else:
                # target이 오른쪽에 포함되면 오른쪽 살펴보기
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                # 아니라면 왼쪽 살펴보기
                else:
                    hi = mid

        return hi if nums[hi] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        """
        [Complexity]
            - TC: O(logn)
            - SC: O(1)

        [Approach]
            앞의 풀이에서 더 명시적으로 경계 조건을 판단하도록 수정할 수 있다. (nums[mid] == target이라면 바로 반환)
        """
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # nums[mid] == target인 경우 곧바로 반환 (명시적)
            if nums[mid] == target:
                return mid

            # 1) 왼쪽이 sorted
            if nums[lo] <= nums[mid]:
                # target이 왼쪽에 포함되면 왼쪽 살펴보기
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                # 아니라면 오른쪽 살펴보기
                else:
                    lo = mid + 1
            # 2) 오른쪽이 sorted
            else:
                # target이 오른쪽에 포함되면 오른쪽 살펴보기
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                # 아니라면 왼쪽 살펴보기
                else:
                    hi = mid - 1

        return -1
