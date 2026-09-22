from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = Counter(t)

        for i, c in enumerate(s):
            if c in check:
                check[c] -= 1
        for key, val in check.items():
            if val > 0:
                return ""
        else:
            for i in range(len(s)):
                c = s[i]
                if c in check:
                    if check[c] == 0:
                        left = i
                        break
                    check[c] += 1
            right = len(s)-1
            result = s[left:right+1]

            while left < right and 0 <= left:
                if s[right] in check:
                    check[s[right]] += 1
                    if check[s[right]] <= 0:
                        if left < right and len(result) > right - left:
                            result = s[left:right]
                        right -= 1

                    else:
                        while check[s[right]] > 0:
                            left -= 1
                            if s[left] in check:
                                check[s[left]] -= 1
                        if left < right and len(result) > right - left:
                            result = s[left:right]
                        right -= 1
                else:
                    if len(result) > right - left:
                        result = s[left:right]
                    right -= 1
            return result
