class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_len = 0
        seen = {}

        for i, char in enumerate(s):

            seen[char] = seen.get(char, 0) + 1
            # what I wrote initially:     
            # if char not in seen:
            #     seen[char] = 1
            # else:
            #     seen[char] += 1
            max_val = max(list(seen.values()))
            window_len = i - start + 1
            if window_len - max_val  <= k:
                max_len = max(max_len, window_len)
            else:
                seen[s[start]] -= 1
                start += 1

        return max_len
    
    # O(N) time complexity and O(1) space complexity.