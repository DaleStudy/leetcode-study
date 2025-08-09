class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time complexity: O(log n)
        output = 1
        while n > 1:
            remain = n % 2
            n = n // 2
            if remain == 1:
                output += 1
        return output
