# 7기 풀이
# 시간 복잡도: O(n)
#  - 입력 받은 strs 리스트의 길이 만큼 순회하므로
# 공간 복잡도: O(1)
#  - 결과로 반환할 result를 제외하고는 변수만 사용
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for str_ in strs:
            # 아나그램의 key를 동일하게 만든다. 갖고 있는 문자열의 오름차순 결과를 key로 만듦
            anagram_key = "".join(sorted(list(str_)))
            # 같은 key를 가진 것끼리 리스트로 묶어둔다.
            result[anagram_key].append(str_)

        return list(result.values())
