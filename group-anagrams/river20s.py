import collections
from typing import List

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            anagram_groups[key].append(s)
        return list(anagram_groups.values())
