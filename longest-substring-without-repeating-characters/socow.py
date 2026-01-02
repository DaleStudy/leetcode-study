"""
📚 3. Longest Substring Without Repeating Characters

📌 문제 요약
- 주어진 문자열 s에서 중복 문자가 없는 가장 긴 부분 문자열의 길이 찾기
- 예: "abcabcbb" → "abc" → 3

🎯 핵심 알고리즘
- 패턴: 슬라이딩 윈도우 (Sliding Window) + 해시맵
- 시간복잡도: O(n)
- 공간복잡도: O(min(n, m)) - m은 문자 집합 크기

💡 핵심 아이디어
1. left, right 두 포인터로 윈도우 관리
2. 해시맵에 각 문자의 마지막 위치 저장
3. 중복 발견 시 → left를 중복 문자 다음으로 점프!
4. 매 단계마다 윈도우 크기(right - left + 1) 최댓값 갱신
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # 문자 → 마지막 인덱스
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # 중복 문자가 현재 윈도우 안에 있으면
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # 중복 다음으로 점프
            
            char_index[char] = right  # 현재 위치 갱신
            max_len = max(max_len, right - left + 1)
        
        return max_len


# Set을 사용한 방식 (더 직관적)
class SolutionWithSet:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 중복이 사라질 때까지 left 이동
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len

