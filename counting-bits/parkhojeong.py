class Solution:
    def countBits(self, n: int) -> list[int]:
        def count(n: int) -> int:
            cnt = 0
            while n > 0:
                cnt += n % 2
                n = n // 2

            return cnt

        output = []
        for i in range(n + 1):
            output.append(count(i))

        return output
