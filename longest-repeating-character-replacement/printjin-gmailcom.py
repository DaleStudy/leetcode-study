class Solution:
    def characterReplacement(self, s, k):
        count = [0] * 26
        left = 0
        max_count = 0
        res = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[right]) - ord('A')])
            while (right - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
