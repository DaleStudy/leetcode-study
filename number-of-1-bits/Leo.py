class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n:
            counter += 1
            n = n & (n - 1)

        return counter

        ## TC: O(k), SC: O(1), since given int(n) has constant length

        # counter = 0

        # for i in bin(n):
        #     if i == "1":
        #         counter += 1

        # return counter
