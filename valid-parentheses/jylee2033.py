class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = [] # Open brackets

        if len(s) % 2 == 1:
            return False

        for ch in s:
            # Open bracket
            if ch in close_to_open.values():
                stack.append(ch)
            # Close bracket
            else:
                if len(stack) == 0:
                    return False

                expected = close_to_open[ch]
                if stack.pop() != expected:
                    return False

        return len(stack) == 0

# Time Complexity: O(n)
# Space Complexity: O(n)
