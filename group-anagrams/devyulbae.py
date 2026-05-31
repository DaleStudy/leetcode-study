"""
Blind 75 - Group Anagrams
LeetCode Problem: https://leetcode.com/problems/group-anagrams/
시간복잡도 : O(N * K) (N은 strs의 길이, K는 strs 내 문자열의 최대 길이)
공간복잡도 : O(N * K)
풀이 : 해시맵을 이용한 풀이
ASCII 문자를 이용하여 각 문자열의 문자 개수를 세어 이를 키로 사용하여 해시맵에 저장한다

"""

from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())
    
