# S and T are the lengths of strings s and t respectively.
# TC: O(S + T) - expanding and contracting sliding window with frequency counts
# SC: O(S + T) - hash tables store frequency counts of unique characters


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        window_counts = {}

        have = 0
        need = len(target_counts)

        res = [-1, -1]
        res_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window_counts[left_char] -= 1

                if (
                    left_char in target_counts
                    and window_counts[left_char] < target_counts[left_char]
                ):
                    have -= 1

                left += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
