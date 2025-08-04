class Solution:
    """
        - Time Complexity: O(n^2), n = len(s)
        - Space Complexity: O(1)
    """
    def countSubstrings(self, s: str) -> int:
        count = 0

        def checkSide(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        
        for i in range(len(s)):
            count += checkSide(i, i)        # Odd case
            count += checkSide(i, i + 1)    # Even case
        
        return count

tc = [
        ("abc", 3),
        ("aaa", 6)
]

sol = Solution()
for i, (s, e) in enumerate(tc, 1):
    r = sol.countSubstrings(s)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
