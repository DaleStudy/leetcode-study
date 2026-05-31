class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = [word]
            else:
                anagram_map[key].append(word)

        return list(anagram_map.values())
    
# Time Complexity: O(N * K log K), N - number of strings, K - maximum length of a string (for sorting)
# Space Complexity: O(N * K)
