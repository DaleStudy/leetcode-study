"""
시간복잡도: O(n)
  - n: 입력된 숫자 n까지의 범위
공간복잡도: O(n)
  - n: 결과값 리스트(ans)의 크기
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = (i & 1) + ans[i // 2]

        return ans
