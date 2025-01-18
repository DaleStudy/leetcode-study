'''
# 20. Valid Parentheses

use stack data structure to perform as a LIFO

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

#### TC is O(n):
- iterating through the string just once to check if the parentheses are valid. = O(n)

#### SC is O(n):
- using a stack to store the parentheses. = the worst case is O(n)
- using a map to store the parentheses. = O(1)

> for space complexity, fixed space is O(1).
> 👉 parentheses_map is fixed and its size doesn't grow with the input size.
> 👉 if the map has much larger size? the space complexity is still O(1).
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # SC: O(n)
        parentheses_map = { # SC: O(1)
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for char in s: # TC: O(n) 
            if char in parentheses_map:
                stack.append(char)
            else:
                if len(stack) == 0 or parentheses_map[stack.pop()] != char:
                    return False
        
        return not stack
