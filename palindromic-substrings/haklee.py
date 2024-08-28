"""TC: O(n^2), SC: O(1)

SC는 sol이라는 카운터 값만 관리하고 있으므로 O(1).

TC는
- 팰린드롬의 중심점의 위치가 range(l)로 주어지므로 여기서 O(n),
- 중심점에서 시작과 끝을 한 칸씩 늘려가면서 팰린드롬 체크할때 O(1),
- 시작과 끝이 최대로 늘어날 수 있는 길이가 O(n),
즉, O(n^2).
"""


class Solution:
    def countSubstrings(self, x: str) -> int:
        l = len(x)
        sol = 0

        for i in range(l):
            # 시작과 끝이 일치하는 상태에서 시작.
            # 즉, 팰린드롬의 길이가 홀수.
            s = e = i
            b = True
            while b:
                sol += (b := (0 <= s and e < l and x[s] == x[e]))
                s -= 1
                e += 1

            # 시작과 끝이 하나 차이나는 상태에서 시작.
            # 즉, 팰린드롬의 길이가 짝수.
            s = e = i
            e += 1
            b = True
            while b:
                sol += (b := (0 <= s and e < l and x[s] == x[e]))
                s -= 1
                e += 1

        return sol
