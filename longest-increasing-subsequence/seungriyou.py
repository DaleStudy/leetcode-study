# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n)

        [Approach]
            dp[i] = nums[i]가 포함되는 LIS의 최대 길이
        """
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [Complexity]
            - TC: O(nlogn) (w. binary search)
            - SC: O(n)

        [Approach]
            ref: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn
            nums를 순차적으로 순회하며 LIS를 모은다. 이때,
                - 현재 보고 있는 원소 n이 LIS의 마지막 원소 이하라면: LIS의 원소 중 (1) n 이상이면서 (2) 최솟값의 위치에 n 덮어쓰기
                - 그 외의 경우라면: LIS의 맨 끝에 num append
            한다.
            LIS는 정렬되어 있을 것이므로 binary search를 이용할 수 있으며, 이렇게 구성한 LIS의 길이가 최대 길이이다.
        """

        def find_leftmost_idx(lis, n):
            lo, hi = 0, len(lis) - 1

            while lo < hi:
                mid = lo + (hi - lo) // 2
                if lis[mid] < n:  # -- 아예 제외하는 경우: n 미만인 경우
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        lis = []

        for n in nums:
            # 현재 보고 있는 n이 LIS의 마지막 원소 이하라면
            if lis and n <= lis[-1]:
                lis[find_leftmost_idx(lis, n)] = n
            # 그 외의 경우라면
            else:
                lis.append(n)

        return len(lis)
