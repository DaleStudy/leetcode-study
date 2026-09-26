class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]

        arr = [0, 1]
        def count(n: int) -> int:
            return arr[n // 2] + n % 2

        for i in range(2, n + 1):
            arr.append(count(i))

        return arr
