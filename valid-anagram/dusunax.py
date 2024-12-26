'''
# Leetcode 242. Valid Anagram

use `Counter` to (1)compare the frequency of characters in both strings, and (2)try to compare the frequency more efficiently. 🔍

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### A. use frequency object

#### TC is O(n):
- iterating through the strings just once to compare the frequency of characters. O(n)

#### SC is O(n):
- creating a new string `converted_s` to store the 

### B. use Counter more efficiently

#### TC is O(n):
- iterating through the strings just once to compare the frequency of characters. O(n)

#### SC is O(n):
- creating a new string `converted_s` to store the 
'''
class Solution:
    def isAnagramA(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = Counter(s) # SC: O(n)

        for char in t: # TC: O(n)
            if char not in frequency or frequency[char] == 0: # TC: O(1)
                return False
            frequency[char] -= 1

        return True
    
    def isAnagramB(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # TC: O(n), SC: O(n)
