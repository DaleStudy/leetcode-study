from collections import defaultdict


class Solution:
    # O(n*mlogm), n = len(str), m = the length of the longest string
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)
        for s in strs:
            group[''.join(sorted(s))].append(s)
        return list(group.values())
