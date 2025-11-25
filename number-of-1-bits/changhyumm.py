class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # 시간복잡도 O(log n) 반으로 나누기 때문
        while n > 0:
            if n % 2 == 1:
                count += 1
                n = n // 2
            else:
                n = n / 2
        return count