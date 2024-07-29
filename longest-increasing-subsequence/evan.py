import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            # num이 왼쪽에 삽입될 수 있는 위치
            position = bisect.bisect_left(lis, num)

            # num이 lis에 있는 모든 요소 보다 크다
            if position == len(lis):
                lis.append(num)
            else:
                lis[position] = num

        return len(lis)
