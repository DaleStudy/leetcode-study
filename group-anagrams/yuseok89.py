# TC: O(N * LlogL)
# SC: O(N * L)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            ans[''.join(sorted(s))].append(s)

        return list(ans.values())

