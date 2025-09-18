class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_count = 0
        res = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_count = max(max_count, counts[s[right]])

            while (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
