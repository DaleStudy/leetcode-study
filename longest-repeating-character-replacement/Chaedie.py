"""
Solution: 
    1) sliding window 활용
    2) window 에 들어가는 글자들은 counts 라는 hash map 으로 갯수를 세어준다.
    3) 순회를 하면서 window size 가 counts에서 가장 큰숫자 + k 보다 크면 invalid window 이기에 left 글자 갯수를 빼고 포인터를 이동해준다.
    4) max_count 는 기존 max 값과 현재 window 사이즈 중 큰 숫자를 셋해준다.

Time: O(n) = O(26n)
Space: O(1) = O(26)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_count = 0

        l, r = 0, 0
        while l <= r and r < len(s):
            counts[s[r]] += 1
            window_size = r - l + 1

            if window_size > max(counts.values()) + k:
                counts[s[l]] -= 1
                l += 1

            window_size = r - l + 1
            max_count = max(window_size, max_count)
            r += 1

        return max_count
