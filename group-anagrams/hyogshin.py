"""
풀이 방법
- ord 함수를 이용해서 캐릭터 수를 기준으로 애너그램 구분
- tuple 활용해서 키로 사용

시간 복잡도: O(n * k)
- 중첩 for loop: O(n * k)

공간 복잡도: O(n)
- cnt 문자열: O(1)
- groups dict: O(n)
"""

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

