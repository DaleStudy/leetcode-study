class Solution:
    """
    binary로 변환 후 zfill로 32자리를 맞춰주고 reverse시킨다.
    """
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
