"""
Blind75 - length of longest substring without repeating characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
시간복잡도 : O(n)
공간복잡도 : O(min(m, n)) (문자 집합 char_index_map의 크기, 최대는 n = len(s))
풀이 : 슬라이딩 윈도우 기법을 사용한 문자열 순회
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        start = 0
        char_index_map = {}

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
                char_index_map[char] = i
            else:
                char_index_map[char] = i
                max_count = max(max_count, i - start + 1)

        return max_count
    
