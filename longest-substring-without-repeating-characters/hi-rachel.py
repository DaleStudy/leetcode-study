"""
문자열 s가 주어졌을 때, 중복된 문자를 제거하고 가장 긴 연속된 substring을 찾아라

1. 첫번째 풀이

Hint!
Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.

TC: O(N^3)
SC: O(N)
=> Time Limit Exceeded

2. 최적화 - 슬라이딩 윈도우 + 해시셋
- 슬라이딩 윈도우: 문자열 내에서 left, right 포인터로 범위를 정하고 점진적으로 이동
- 해시셋: 현재 윈도우에 어떤 문자가 있는지 빠르게 체크 가능
- 중복 문자가 등장하면 왼쪽 포인터를 이동시켜서 중복을 제거

TC: O(N)
SC: O(N)
"""

# Time Limit Exceeded 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        # Generate all possible substrings without duplicate characters
        def make_all_substrings(string):
            nonlocal max_len
            n = len(string)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    k = len(string[i:j])
                    if k == len(list(set(string[i:j]))):  # if it's valid
                        max_len = max(k, max_len)  # keep updating maxLen accordingly

        make_all_substrings(s)
        return max_len
    

# 최적화 - 슬라이딩 윈도우 + 해시셋 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 현재 윈도우에 있는 문자들
        left = 0
        max_len = 0

        for right in range(len(s)):
            # 중복 문자가 나오면 왼쪽 포인터를 이동시켜 중복 제거
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # 중복이 없으면 윈도우에 추가
            char_set.add(s[right])

            # 최대 길이 갱신
            max_len = max(max_len, right - left + 1)
            
        return max_len


# HashMap 풀이
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
 
    left = 0  # 윈도우 시작점
    max_length = 0  # 최대 길이
    seen = {}  # 문자의 마지막 등장 위치를 저장하는 해시맵
 
    for right in range(len(s)):
        char = s[right]
 
        # 현재 문자가 윈도우 내에 이미 존재하는 경우
        if char in seen and seen[char] >= left:
            # 윈도우 시작점을 중복 문자 다음 위치로 이동
            left = seen[char] + 1
 
        # 현재 문자의 위치 업데이트
        seen[char] = right
 
        # 현재 윈도우 길이와 최대 길이 비교 후 업데이트
        max_length = max(max_length, right - left + 1)
 
    return max_length