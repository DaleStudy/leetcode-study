import collections

class Solution:
    def hammingWeight(self, n: int) -> int:
        two_digit = []
        while n >= 1:
            two_digit.append(n % 2)
            n = n // 2
        cnt_dict = collections.Counter(two_digit)
        return cnt_dict[1]
    