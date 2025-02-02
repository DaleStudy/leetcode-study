'''
# 424. Longest Repeating Character Replacement

use sliding window to find the longest substring with at most k replacements.

## Time and Space Complexity

```
TC: O(n)
SC: O(1)
```
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26 # A~Z, SC: O(1)
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)): # TC: O(n)
            curr_char_index = ord(s[right]) - 65
            freq[curr_char_index] += 1
            max_freq = max(max_freq, freq[curr_char_index])
            
            if (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - 65] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
