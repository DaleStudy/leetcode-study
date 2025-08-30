from typing import List
from collections import Counter, defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         dict_anagrams = defaultdict(list)
#         for idx, word in enumerate(strs):
#             key = tuple(sorted(Counter(word).items()))
#             dict_anagrams[key].append(word)
#
#         return list(dict_anagrams.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            dict_anagrams[key].append(word)

        return list(dict_anagrams.values())
