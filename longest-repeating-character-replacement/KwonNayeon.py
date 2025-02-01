"""
Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length

Time Complexity: O(n)
- 여기서 n은 문자열의 길이

Space Complexity: O(1)
- 추가 변수(left, right, max_length 등)는 상수 개

풀이방법:
1. Sliding Window로 구간을 관리
- right 포인터로 구간을 늘리다가
- 변경해야하는 문자 수가 k를 초과하면 left 포인터로 구간을 줄임

2. 각 구간에서:
- 가장 많이 등장한 문자로 나머지를 변경
- (구간 길이 - 가장 많이 등장한 문자 수)가 k 이하여야 함
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1

            curr_length = right - left + 1

            if curr_length - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length
