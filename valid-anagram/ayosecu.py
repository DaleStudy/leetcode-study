from collections import Counter

class Solution:
    """
        - Time Complexity: O(n + m), n = len(s), m = len(t)
        - Space Complexity: O(n + m)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

tc = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("abc", "dcba", False)
]

for i, (s, t, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.isAnagram(s, t)
    print(f"TC {i} is Passed!" if e == r else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
