from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = defaultdict(int)
        for s1 in s:
            char_map[s1] += 1

        contrast_map = defaultdict(int)
        for t1 in t:
            contrast_map[t1] += 1

        for key, val in char_map.items():
            contrast_val = contrast_map[key]
            if contrast_val != val:
                return False

        for key, val in contrast_map.items():
            char_val = char_map[key]
            if char_val != val:
                return False

        return True

