'''
시간복잡도: O(n)
- right와 left 포인터가 각각 최대 n번 움직임

공간복잡도: O(n)
- hars 집합이 최대 n개의 고유 문자를 저장할 수 있
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0
        chars = set()

        for right in range(len(s)):
            if s[right] in chars:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
            chars.add(s[right])
            length = max(length, right + 1 - left)

        return length
