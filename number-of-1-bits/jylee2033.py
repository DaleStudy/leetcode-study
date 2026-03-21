class Solution:
    def hammingWeight(self, n: int) -> int:
        # # 1. Find highest power of 2 range that covers n
        # # 2. Greedily subtract from largest power of 2 to smallest

        # # powers : 1 + 2 + 4 +  8 + 16 + ...
        # # total  : 1 + 3 + 7 + 15 + 31 + ...
        # # index  : 0   1   2    3    4

        # i = 0
        # total = 1

        # while n > total:
        #     i += 1
        #     total += 2 ** i

        # count = 0

        # for j in range(i, -1, -1):
        #     if n >= 2 ** j:
        #         n -= 2 ** j
        #         count += 1

        # return count

# Time Complexity : O(log n)
# Space Complexity : O(1)

        count = 0

        while n > 0:
            if n % 2 == 1:
                count += 1

            n //= 2

        return count

# Time Complexity : O(log n)
# Space Complexity : O(1)
