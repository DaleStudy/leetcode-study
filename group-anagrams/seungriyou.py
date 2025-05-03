# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        [Approach]
            - TC: O(n * klogk) (n = len(strs), k = max length of an element)
            - SC: O(n * k)

        [Complexity]
            (1) strs의 원소들을 정렬해서 (2) hash table의 key 값으로 사용하면
            매 단계마다 O(1)에 anagram을 찾을 수 있다.
            이때, key 값으로는 list는 사용할 수 없고, string이나 tuple을 사용해야 한다.
        """
        from collections import defaultdict

        anagrams = defaultdict(list)

        for s in strs:
            anagrams["".join(sorted(s))].append(s)

        return list(anagrams.values())
