class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)

    def reverse_bits(self, n: int):
        result = 0
        for i in range(32):
            lsb = n & 1
            result <<= 1
            result |= lsb
            n >>= 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.reverse_bits(10))
