class Solution:
    # Time Complexity: O(n), n: len(strs)
    # Space Complexity: O(n), n: len(strs)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()  # key: string in an alphabetical order, values: strings

        for s in strs:
            word = ''.join(sorted(s))
            if word in anagram_groups:
                anagram_groups[word].extend([s])
            else:
                anagram_groups[word] = [s]

        return list(anagram_groups.values())
