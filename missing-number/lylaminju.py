from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # 0부터 n까지의 숫자의 합을 수학적 합 공식을 사용해 계산
        total_sum = n * (n + 1) // 2

        return total_sum - sum(nums)

# 시간 복잡도 O(n)
# 공간 복잡도 O(1)
