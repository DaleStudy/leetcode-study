from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            if not s:
                d["0"].append("")
            else:
                d["".join(sorted(s))].append(s)

        return [d[s] for s in d]
