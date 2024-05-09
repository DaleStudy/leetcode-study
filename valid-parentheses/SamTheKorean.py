# Time complexity : O(n)
# Space complexity : O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"[": "]", "{": "}", "(": ")"}
        stack = []

        # if ch is opening bracket
        for ch in s:
            if ch in parentheses:
                stack.append(ch)
            # if ch is closing bracket
            else:
                # if closing bracket comes without opening bracket previously
                if not stack:
                    return False
                # if closing bracket doesnt match with the latest type of opening bracket
                if ch != parentheses[stack.pop()]:
                    return False

        # True if stack is empty after going through the process above
        return not stack
