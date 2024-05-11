# TC, SC: O(n), O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for c in s:
            if c in ["(", "[", "{"]:
                arr.append(c)
                continue
            else:
                if not arr:
                    return False
                b = arr.pop()
                if b == "(" and c == ")":
                    continue
                if b == "[" and c == "]":
                    continue
                if b == "{" and c == "}":
                    continue
                return False
        if arr:
            return False
        else:
            return True
