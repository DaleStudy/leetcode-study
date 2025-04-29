"""
Time complexity O(n)
Space compexity O(n)

hash table, sorting
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            sorted_str = str(sorted(s))
            group[sorted_str].append(s)
        
        return list(group.values())
