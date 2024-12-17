'''
# Leetcode 125. Valid Palindrome

use `isalnum()` to filter out non-alphanumeric characters 🔍

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through the string just once to filter out non-alphanumeric characters. O(n)

### SC is O(n):
- `s.lower()` creates a new string. O(n)
- creating a new string `converted_s` to store the filtered characters. O(n)
- `converted_s[::-1]` creates a new reversed string. O(n)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True

        s = s.lower()
        converted_s = ''.join(c for c in s if c.isalnum())

        return converted_s == converted_s[::-1]

