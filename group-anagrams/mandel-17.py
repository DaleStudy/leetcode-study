import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            result[''.join(sorted(s))].append(s)                
        return list(result.values())      

