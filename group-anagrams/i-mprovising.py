"""
Time complexity O(n)
--> O(n * wlog(w))
n : 주어지는 단어 개수
w : 평균 단어 길이

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
