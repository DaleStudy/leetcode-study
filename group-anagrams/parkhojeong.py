class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        for s in strs:
            key = "".join(sorted(s))
            anagram_dic.setdefault(key, []).append(s)

        return list(anagram_dic.values())
