"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

문제: 문자열 배열이 주어질 때, 애너그램끼리 그룹으로 묶어서 반환하라.
     애너그램 = 같은 문자들로 이루어진 단어 (순서만 다름)

예시:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    
    "eat", "tea", "ate" → 모두 a, e, t로 구성 → 같은 그룹
    "tan", "nat" → 모두 a, n, t로 구성 → 같은 그룹
    "bat" → 혼자 → 별도 그룹
"""


# =============================================================================
# 풀이 1: 정렬(Sorted)을 키로 사용
# =============================================================================
# 아이디어: 애너그램은 정렬하면 같은 문자열이 된다!
#          "eat" → "aet", "tea" → "aet", "ate" → "aet"
#          정렬된 문자열을 딕셔너리의 키로 사용하여 그룹화
#
# 시간 복잡도: O(n * k log k)
#   - n: 문자열 개수
#   - k: 가장 긴 문자열의 길이
#   - 각 문자열을 정렬하는데 O(k log k)
#
# 공간 복잡도: O(n * k) - 모든 문자열을 딕셔너리에 저장
# =============================================================================
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}  # 일반 딕셔너리

        for word in strs:
            sorted_key = "".join(sorted(word))
            
            # 키가 없으면 먼저 빈 리스트 생성
            if sorted_key not in anagram_map:
                anagram_map[sorted_key] = []
            
            # 그 다음 append
            anagram_map[sorted_key].append(word)

        return list(anagram_map.values())
