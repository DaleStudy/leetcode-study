# TC : O(nwlog(w))
# reason : n being the number of words and w being the length of each word, therefore the total time complexity is n times wlog(w) (time complexity for sorting each word)
# SC : O(w*n)
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        # Use sorted word as a string and append it with the original word so the word containing same charactors with the same number of existence can be in the same group
        for word in strs:
            anagrams[str(sorted(word))].append(word)

        return anagrams.values()
