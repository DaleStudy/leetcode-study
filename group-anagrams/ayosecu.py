from typing import List
from collections import defaultdict

class Solution:
    """
        - Time Complexity: O(nklogk), n = len(strs), k = Max of len(strs[i])
            - for loop => O(n)
            - sorted(s) => O(klogk)
        - Space Complexity: O(nk), dictionary size
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary
        dic = defaultdict(list)

        for s in strs:
            ss = "".join(sorted(s))
            dic[ss].append(s)
        
        return list(dic.values())

tc = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
]

for i, (strs, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.groupAnagrams(strs)
    r_sorted = sorted([sorted(group) for group in r])
    e_sorted = sorted([sorted(group) for group in e])    
    print(f"TC {i} is Passed!" if r_sorted == e_sorted else f"TC {i} is Failed! - Expected: {e_sorted}, Result: {r_sorted}")
