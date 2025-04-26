class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        Time complexity: O(1)
        Space complexity: O(1)
        """
        count = 0
        for _ in range(32):
            count += n & 1
            n >>= 1
        return count
