"""TC: O(n), SC: O(1)

n은 주어진 문자열의 길이

아이디어:
- 투 포인터를 써서 문자열의 시작, 끝을 관리하면서 부분 문자열을 만든다.
- 부분 문자열에 들어있는 문자 중 가장 많은 문자와 k의 합이 문자열의 길이 보다 크면 조건 만족.
- 부분 문자열에 들어있는 문자 개수를 dict를 써서 관리하자.

SC:
- 부분 문자열에 들어있는 문자 개수를 관리하는 dict에서 O(1).
- 부분 문자열의 시작, 끝 인덱스 관리 O(1).
- 종합하면 O(1).

TC:
- 부분 문자열의 끝 인덱스를 하나 늘릴 때마다 반환할 값 업데이트. O(1)을 n번 시행하므로 O(n).
- 시작, 끝 인덱스 수정할 때마다 부분 문자열에 들어있는 문자 개수 업데이트. 시작, 끝 인덱스는
  많이 수정해봐야 합쳐서 2*n번. 즉, O(1)을 2*n번 시행하므로 O(n).
- 시작, 끝 인덱스에 1을 더하는 시행. O(1)을 2*n번 시행하므로 O(n).
- 종합하면 O(n).
"""


class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        char_cnt = {c: 0 for c in set(string)}
        s = e = 0
        sol = -1
        while e < len(string):
            char_cnt[string[e]] += 1
            while e - s + 1 > max(char_cnt.values()) + k:
                char_cnt[string[s]] -= 1
                s += 1
            sol = max(e - s + 1, sol)
            e += 1
        return sol
