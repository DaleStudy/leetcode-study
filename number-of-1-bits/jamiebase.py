"""
# Intuition
n을 n-1과 AND 비트 연산하면서 1을 제거해나가며 카운트한다.

# Complexity
- Time complexity: n의 이진수 변환에서 1의 개수를 K라고 할 때, O(K)

- Space complexity: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
