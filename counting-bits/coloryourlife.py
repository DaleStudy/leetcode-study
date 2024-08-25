# T: O(N)
# S: O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            m = i
            cnt = 0
            while m > 0:
                if m & 1 == 1:
                    cnt += 1
                m = m >> 1
            res.append(cnt)
        return res

