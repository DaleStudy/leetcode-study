class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        sol 1
        Runtime: Beats 78.74% / O(N)
        Memory: Beats 64.30% / O(1)
        '''
        s_dict = dict()
        for elem in s:
            try:
                s_dict[elem] += 1
            except Exception as ex:
                s_dict[elem] = 1
        for elem in t:
            try:
                s_dict[elem] -= 1
            except Exception as ex:
                return False
        return not (any(s_dict.values()))

        '''
        sol 2
        Runtime: Beats 72.12% / O(N)
        Memory: Beats 97.51% / O(1)
        '''
        from itertools import zip_longest
        from collections import defaultdict

        ana_dict = defaultdict(int)
        for elem1, elem2 in zip_longest(s, t):
            ana_dict[elem1] += 1
            ana_dict[elem2] -= 1
        return not (any(ana_dict.values()))


