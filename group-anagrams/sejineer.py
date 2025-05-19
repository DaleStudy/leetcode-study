"""
시간 복잡도: O(N * K) N=문자열 개수, 평균 문자열 길이 = K (최대 100)
공간 복잡도: O(N * K) 
"""
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for s in strs:
            s_counter = Counter(s)
            strs_dict[frozenset(s_counter.items())].append(s)
        
        return list(strs_dict.values())
