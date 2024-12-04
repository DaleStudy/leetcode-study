'''
# Leetcode 125. Valid Palindrome

use regex to filter out non-alphanumeric characters 🔍

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- iterating through the string just once to filter out non-alphanumeric characters.

### SC is O(n):
- creating a new string to store the filtered characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is " ":
            return True

        reg = "[^a-z0-9]"
        converted_s = re.sub(reg, "", s.lower())

        return converted_s == converted_s[::-1]
