"""
# Approach
strs 배열을 순회하며 문자열을 정규화(정렬)하고,
정규화 값이 같은 원소들끼리 모이도록 딕셔너리에 추가하여 최종 값을 반환한다.

# Complexity
strs의 길이를 N, 문자열의 길이를 K라고 할 때,

- Time complexity:  O(N*KlogK)
- Space complexity: O(N*K)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = defaultdict(list)  # normalized str : str list
        for s in strs:
            anagram["".join(sorted(s))].append(s)
        return list(anagram.values())
