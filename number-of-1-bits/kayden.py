# 시간복잡도: O(log N)
# 공간복잡도: O(log N)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")