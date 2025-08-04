"""
Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length

Time Complexity: O(n)
- 여기서 n은 문자열의 길이

Space Complexity: O(1)
- 추가 변수(max_length, max_count, start, end 등) 이외의 공간 사용하지 않음

풀이방법:
1. Sliding Window로 구간을 관리
- end 포인터로 구간을 늘리다가
- 변경해야하는 문자 수가 k를 초과하면 start 포인터로 구간을 줄임

2. 각 구간에서:
- 나머지 문자를 가장 많이 등장한 문자로 변경
- (구간 길이 - 가장 많이 등장한 문자 수)가 k 이하여야 함
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        max_length = 0
        max_count = 0
        start = 0
        char_count = defaultdict(int)

        for end in range(len(s)):
            # 현재 문자의 등장 횟수 증가
            char_count[s[end]] += 1

            # 윈도우 내 가장 많이 나타난 문자의 등장 횟수 업데이트
            max_count = max(max_count, char_count[s[end]])

            # 윈도우의 크기 - 가장 많이 나타난 문자의 등장 횟수 = 변경해야 할 문자의 수
            # 이 때 변경하는 문자의 종류는 상관없음
            # 이 값이 k보다 클 때, 윈도우의 크기를 줄임
            if (end - start + 1) - max_count > k:
                char_count[s[start]] -= 1
                start += 1

            # 최대 길이 업데이트
            max_length = max(max_length, end - start + 1)
            
        return max_length
