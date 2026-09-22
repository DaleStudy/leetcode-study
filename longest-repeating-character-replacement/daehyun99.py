# Time: O(n)
# Space: O(1)
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

"""
# Time: O(n)
# Space: O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find_bunch()
        bunch = []
        start_idx = 0
        start_word = s[0]
        for i in range(1, len(s)):
            if s[i] != start_word:
                bunch.append([start_word, i- start_idx])
                start_word = s[i]
                start_idx = i
        bunch.append([start_word, len(s) - start_idx])

        # find_LRCR()
        unique = set([c for c in s])
        result = 0

        for base in unique:
            changed_num = 0
            left = 0
            right = 0
            length = 0
            while right < len(bunch):
                if bunch[right][0] != base:
                    changed_num += bunch[right][1]
                length += bunch[right][1]
                right += 1

                while changed_num > k:
                    if bunch[left][0] != base:
                        changed_num -= bunch[left][1]
                    length -= bunch[left][1]
                    left += 1
                result = max(result, min(length + k - changed_num, len(s)))
        return result
"""
