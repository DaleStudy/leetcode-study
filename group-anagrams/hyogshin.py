from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      groups = defaultdict(list)
      for s in strs:
        cnt = [0] * 26
        for ch in s:
          cnt[ord(ch) - ord('a')] += 1
        groups[tuple(cnt)].append(s)
      return list(groups.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
