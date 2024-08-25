"""TC: O(n), SC: O(n)

여기서 n은 s, t의 길이값 중 큰 것이라 가정.

SC:
- Counter는 s, t에 들어있는 글자들을 key로 하는 dict. 즉, SC는 O(n).

TC:
- s, t에 들어있는 글자들을 key로 dict를 업데이트를 한 번 할때 O(1).
- 위의 과정을 길이 n만큼 반복하므로 O(n).
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)  # TC: O(n log n), SC: O(n)
        return Counter(s) == Counter(t)  # TC: O(n), SC: O(n)
