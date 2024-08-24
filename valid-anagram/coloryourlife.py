class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. sorting and compare : O(nlogn)
        # 2. hashing: O(n)
        # 3. array: O(n)
        if len(s) != len(t):
            return False
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        
        for c in t:
            char_dict[c] -= 1
            if char_dict[c] < 0:
                return False
        
        return True

