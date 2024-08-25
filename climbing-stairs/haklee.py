"""TC: O(n), SC: O(1)

아이디어: 
계단의 k번째 칸까지 도달하는 방법의 수를 f(k)라고 하자.
f(k)는 다음의 두 경우의 수를 더한 값이다.
  - k-2번째 칸까지 간 다음 두 칸 뜀. 즉, f(k-2)
  - k-1번째 칸까지 간 다음 두 칸 뜀. 즉, f(k-1)
즉, f(k) = f(k-2) + f(k-1)


SC:
- tabulation 과정에서 값 2개만 계속 유지한다.
- 즉, O(1).

TC:
- 단순 덧셈 계산(O(1))을 O(n)번 반복한다.
- 즉, O(n).
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
