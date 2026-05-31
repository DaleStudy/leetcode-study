# idea: sorting and dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = str(sorted(word)) #sorted returns list
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        return list(anagrams.values())


