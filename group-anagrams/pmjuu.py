# 시간 복잡도: O(n * m log m)
# - n: 문자열 배열의 길이, m: 각 문자열의 최대 길이
# - 각 문자열을 정렬하는 데 O(m log m) 시간이 걸리며, 모든 문자열에 대해 이를 수행
# - 문제에서 m 이 최대 100이므로, 정렬 비용은 상수에 가깝게 볼 수도 있음 (m = 100인 상황에서 100 * log(100)는 약 664 정도)

# 공간 복잡도: O(n * m)
# - 정렬된 문자열(길이 최대 m)을 키로 사용하는 딕셔너리에 최대 n개의 키가 생길 수 있음
# - 각 키에 대해 원본 문자열들을 저장하므로 O(n * m) 크기의 공간을 사용

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
