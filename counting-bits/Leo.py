class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]

        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2)

        return counter

        ## TC: O(n), SC: O(n)
        ## this question should be under math section tbh
