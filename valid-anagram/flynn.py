'''
For N, length of the given strings,

Time Complexity: O(N)
- first iteration: O(N)
- second iteration: O(N)

Space Compelxity: O(N)
- dictionaries for each strings: O(N)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        for c in count_s:
            if c not in count_t or count_s[c] != count_t[c]:
                return False
        return True
