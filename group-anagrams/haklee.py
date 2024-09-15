"""TC: O(n * l * log(l)), SC: O(n * l)

전체 문자열 개수 n개, 문자열 최대 길이 l.

아이디어:
- 모든 문자열에 대해 해당 문자열을 이루는 문자 조합으로 고유한 키를 만드는 것이 주된 아이디어.
    - 문자열을 해체해서 sort한 다음 이를 바로 tuple로 만들어서 키로 사용했다.
- list를 리턴하라고 되어있는 것을 `dict_values`로 리턴했지만 문제가 생기지 않아서 그냥 제출했다.

SC:
- dict 관리.
    - 키값 최대 n개, 각각 최고 길이 l. O(n * l).
    - 총 아이템 n개, 각각 최고 길이 l. O(n * l).
- 종합하면 O(n * l).

TC:
- strs에 있는 각 아이템을 sort함. O(l * log(l))
- 위의 과정을 n번 반복.
- 종합하면 O(n * l * log(l)).
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            # k값 계산이 오른쪽에서 먼저 이루어지는군요?!
            d[k] = d.get(k := tuple(sorted(s)), []) + [s]
        return d.values()


"""TC: O(n * l * log(l)), SC: O(n * l)
각 단어를 sort하는 것보다 단어를 이루고 있는 문자를 카운터로 세어서 이 카운터를 키로 쓰는 것이
시간복잡도에 더 좋을 수도 있다. Counter를 써서 알파벳 개수를 dict로 만든 다음 json.dumps로 str
로 만들어버리자.

실제 이 솔루션을 제출하면 성능이 별로 좋지 않은데, l값이 작아서 위의 과정을 처리하는 데에 오버헤드가
오히려 더 붙기 때문을 추정된다.
"""

from collections import Counter
from json import dumps


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            d[k] = d.get(k := dumps(Counter(s), sort_keys=True), []) + [s]
        return d.values()
