"""
	TC : n의 크기에 상관없이 32번 반복하므로
		O(1)
	SC : 추가적인 메모리 쓰지 않으므로
		O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for _ in range(31) :
            ret |= n & 1
            ret <<= 1
            n >>= 1
        ret |= n & 1
        return ret
