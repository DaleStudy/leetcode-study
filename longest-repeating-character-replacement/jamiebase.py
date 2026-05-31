"""
# Approach
1. 구간에서 제일 많은 문자 찾는다
2. 나머지를 바꾼다
3. 바꾸는 개수가 k 이하인지 본다
4. 가능하면 구간 길이를 키운다

# Complexity
문자열 s에서 서로 다른 글자의 종류 U, s의 길이 N
- Time complexity: O(N)
- Space complexity: O(U) => 영어 대문자만 나오므로 사실상 O(1)
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
