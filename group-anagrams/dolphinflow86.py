# 1) Group words by their sorted form using defaultdict. While iterating the strs, sort each word and append original word to the corresponding list. After then convert dict to 2 dimensional list and return the list. 
# TC: O(N*LlogL) where N is length of strs, L is max length of a word.
# SC: O(N*L)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            groups[sorted_str].append(str)

        return list(groups.values())
