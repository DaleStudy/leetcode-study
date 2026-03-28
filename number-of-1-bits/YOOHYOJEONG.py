# https://leetcode.com/problems/number-of-1-bits

class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)[2:]
        return len(str(binary).replace('0', ''))
