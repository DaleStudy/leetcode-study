class Solution:
    # Time complexity: O(log n)
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n = n // 2
        return cnt
