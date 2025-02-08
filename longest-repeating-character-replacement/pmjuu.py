'''
시간복잡도: O(n)
- 문자열의 길이만큼 한 번만 순회합니다.
공간복잡도: O(n)
- char_count 딕셔너리는 최대 알파벳 26개만 저장합니다.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        max_length = 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])

            # If the remaining characters exceed the allowed k changes
            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
