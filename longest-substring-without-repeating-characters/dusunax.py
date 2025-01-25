'''
# 3. Longest Substring Without Repeating Characters

use a set to store the characters in the current substring.


## Time and Space Complexity

### Solution 1: using set

```
TC: O(n)
SC: O(n)
```

####  TC is O(n):
- iterating with end pointer through the string once. = O(n)
- inner while loop runs at most once for each character in the string. = Amortized O(1)

#### SC is O(n):
- using a set to store the characters in the current substring. = O(n)

### Solution 2: using ASCII array

```
TC: O(n)
SC: O(128)
```

#### TC is O(n):
- iterating with end pointer through the string once. = O(n)
- checking if the character is in the current substring.

#### SC is O(1):
- using an array to store the characters in the current substring. = constant space O(128)
'''
class Solution:
    def lengthOfLongestSubstringWithSet(self, s: str) -> int:
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
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        start = 0
        char_index = [-1] * 128 # SC: O(128)

        for end in range(len(s)): # TC: O(n)
            if char_index[ord(s[end])] >= start:
                start = char_index[ord(s[end])] + 1
            char_index[ord(s[end])] = end
            max_count = max(max_count, end - start + 1)
            
        return max_count
