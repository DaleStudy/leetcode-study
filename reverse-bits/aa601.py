#시간복잡도 : O(1), 공간복잡도 : O(1)

class Solution:
	def reverseBits(self, n: int) -> int:
		ret = 0
		for i in range(32) :
			ret = (ret << 1 | (n & 1))
			n >>= 1
		return (ret)

