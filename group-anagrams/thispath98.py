from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for string in strs:
            anagram_dict[tuple(sorted(string))].append(string)

        answer = list(anagram_dict.values())
        return answer
