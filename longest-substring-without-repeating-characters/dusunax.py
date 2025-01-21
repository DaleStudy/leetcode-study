'''
# 3. Longest Substring Without Repeating Characters

use a set to store the characters in the current substring.


## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- iterating with end pointer through the string once. = O(n)
- inner while loop runs at most once for each character in the string. = Amortized O(1)

#### SC is O(n):
- using a set to store the characters in the current substring. = O(n)

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        start = 0
        substrings = set() # SC: O(n)

        for end in range(len(s)): # TC: O(n)
            while s[end] in substrings: # TC: Amortized O(1)
                substrings.remove(s[start])
                start += 1
            substrings.add(s[end])
            max_count = max(max_count, end - start + 1)
        
        return max_count
