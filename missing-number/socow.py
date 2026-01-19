"""
268. Missing Number

문제 요약
- 0부터 n까지의 숫자 중 하나가 빠진 배열이 주어짐
- 빠진 숫자 찾기!
- 예: [3, 0, 1] → 2가 없음 → 답: 2

문제 예시
nums = [3, 0, 1]  (0, 1, 2, 3 중 하나 빠짐)
→ 2가 없음!
→ return 2

핵심 알고리즘
- 시간복잡도: O(n)
- 공간복잡도: O(1)

핵심 아이디어
- 수학: 0~n 합계 - 배열 합계 = 빠진 숫자!
- XOR: 같은 숫자 XOR하면 0, 남는 게 빠진 숫자!
"""

from typing import List


# 방법 1: 수학 (가장 직관적!)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # 0~n 합계 공식
        actual_sum = sum(nums)           # 실제 합계
        return expected_sum - actual_sum


# 방법 2: XOR (비트 연산)
class SolutionXOR:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)  # n부터 시작
        
        for i, num in enumerate(nums):
            result ^= i      # 인덱스랑 XOR
            result ^= num    # 값이랑 XOR
        
        return result
