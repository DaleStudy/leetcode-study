class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine whether two strings are anagrams.

        Time Complexity: O(n)
        Space Complexity: O(k)
        - n: length of the string
        - k: number of unique characters
        """
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 1
        
        for j in t:
            if j in dic_t:
                dic_t[j] += 1
            else:
                dic_t[j] = 1
        
        return dic_s == dic_t
