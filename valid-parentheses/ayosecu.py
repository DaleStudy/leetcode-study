class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(n)
    """
    def isValid(self, s: str) -> bool:
        open_ch = { "(":")", "{":"}", "[":"]" }
        close_ch = { ")":"(", "}":"{", "]":"[" }
        st = []

        for c in s:
            if c in open_ch:
                st.append(c)
            elif c in close_ch:
                if not st:
                    return False

                if close_ch[c] != st[-1]:
                    return False
                else:
                    st.pop()
            else:
                # Error Cases (Invalid Input)
                return False
        
        return len(st) == 0

tc = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True)
]

sol = Solution()
for i, (s, e) in enumerate(tc, 1):
    r = sol.isValid(s)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
