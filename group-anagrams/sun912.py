"""
    TC: O(m*n)
    SC: O(26*n) -> O(n)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c)-ord("a")] += 1
            result[tuple(count)].append(word)

        return result.values()
