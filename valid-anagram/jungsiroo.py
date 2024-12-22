class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # sort and compare
        # Tc : O(nlogn) / Sc : O(n)(Because of python timsort)
        """
        s = sorted(s)
        t = sorted(t)
        for s_char, t_char in zip(s, t):
            if s_char != t_char:
                return False
        return True
        """

        # dictionary to count letters
        # Tc : O(n) / Sc : O(n)
        letters_cnt = dict()
        INF = int(1e6)
        for s_char in s:
            letters_cnt[s_char] = letters_cnt.get(s_char,0)+1
        
        for t_char in t:
            letters_cnt[t_char] = letters_cnt.get(t_char,INF)-1
            if letters_cnt[t_char] < 0:
                return False

        return sum(letters_cnt.values()) == 0

