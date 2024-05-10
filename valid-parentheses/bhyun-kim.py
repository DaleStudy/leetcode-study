"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Solution
    Uses a stack to check if the parentheses are valid.

    1. Initialize an empty stack.
    2. Iterate through each character in the string.
    3. If the character is an opening parenthesis, 
        push it to the stack.
    4. If the character is a closing parenthesis,
        pop the stack and check if the opening parenthesis matches.
    5. If the stack is empty, return True.
    6. Otherwise, return False.

Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]

        for _s in s:
            if _s in opening:
                stack = _s + stack
            else:
                if stack:
                    if opening[closing.index(_s)] == stack[0]:
                        stack = stack[1:]
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0
