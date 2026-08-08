"""
N: `s`의 길이, M: `s`에서 중복을 제외한 문자의 개수
Time: O(N)
Space: O(min(N,M))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # 문자의 최근 인덱스를 저장
        char_map = {}

        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            char_map[char] = right
            
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len

        return max_len
