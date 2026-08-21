from collections import Counter


class Solution:
    # Time Complexity: O(n), n: s.length
    # Space Complexity: O(1) (as s and t consist of uppercase and lowercase letters. -> fixed value)
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        left, min_len = 0, float('inf')
        target, window = Counter(t), Counter()
        required, satisfied = len(target), 0
        min_start = 0

        for right, ch in enumerate(s):  # expand the window
            window[ch] += 1
            if ch in target and window[ch] == target[ch]:
                satisfied += 1

            # shrink the window
            while left <= right and required == satisfied:
                if right - left + 1 < min_len:
                    min_start = left
                    min_len = right - left + 1

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in target and window[left_ch] < target[left_ch]:
                    satisfied -= 1

                left += 1

        return "" if min_len == float('inf') else s[min_start: min_start + min_len]
