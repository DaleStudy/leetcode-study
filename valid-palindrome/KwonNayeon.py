"""
Conditions:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Time Complexity:
- O(n)
Space Complexity:
- O(n)
"""
# Solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        return False

# Solution 2
