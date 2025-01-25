"""
Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Time Complexity: O(n)
- 문자열을 한번만 순회

Space Complexity: O(n)
- 딕셔너리에 문자와 인덱스 저장

풀이 방법:
1. 슬라이딩 윈도우와 딕셔너리를 활용
2. seen 딕셔너리에 각 문자의 마지막 등장 위치를 저장
3. 중복 문자를 만나면 윈도우의 시작점(current_start)을 중복 문자 다음 위치로 이동
4. 매 단계에서 현재 윈도우의 길이를 계산하고 최대 길이 갱신
5. 최종적으로 가장 긴 중복 없는 부분 문자열의 길이 반환
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        current_start = 0
        max_length = 0

        for i in range(len(s)):
            char = s[i]

            if char in seen and seen[char] >= current_start:
                current_start = seen[char] + 1

            seen[char] = i

            current_length = i - current_start + 1
            max_length = max(current_length, max_length)
        
        return max_length
