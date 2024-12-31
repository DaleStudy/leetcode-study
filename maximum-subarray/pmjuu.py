from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -float('inf')
        current_sum = -float('inf')

        for num in nums:
            current_sum = max(current_sum + num, num)
            largest_sum = max(largest_sum, current_sum)

        return largest_sum


# 시간 복잡도: O(n)
# - nums 배열을 한 번 순회하며 각 요소에 대해 최대 부분 배열 합을 계산하므로 시간 복잡도는 O(n)입니다.
#
# 공간 복잡도: O(1)
# - 추가로 사용하는 변수는 largest_sum과 current_sum 두 개뿐이므로 공간 복잡도는 O(1)입니다.
