"""
# Approach
1) 정수를 이진 문자열로 변환한 뒤,
32비트로 맞추고 뒤집어서 다시 정수로 변환한다.

2) n에서 비트를 하나씩 꺼내서 res에 역순으로 붙인다

# Complexity
- Time complexity: O(1)
- Space complexity: O(1)
"""


# 1
class Solution:
    def reverseBits(self, n: int) -> int:
        b_num = format(n, "b")
        b_reversed = b_num.zfill(32)[::-1]
        return int(b_reversed, 2)


# 2
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
