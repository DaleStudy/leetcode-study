class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        # to lower and check two pointers
        s = s.lower()
        l, r = 0, len(s) - 1

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True


tc = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
]

for i, (s, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.isPalindrome(s)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
