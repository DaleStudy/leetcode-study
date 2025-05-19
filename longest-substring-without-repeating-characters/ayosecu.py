class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_set = set()

        longest_length, length = 0, 0
        l, r = 0, 0
        while r < len(s):
            # check each character (s[r]) is duplicated, and expand or narrow the length
            if s[r] not in check_set:
                check_set.add(s[r])
                length += 1
                longest_length = max(longest_length, length)
                r += 1
            else:
                check_set.remove(s[l])
                length -= 1
                l += 1
        
        return longest_length

tc = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
]

sol = Solution()
for i, (s, e) in enumerate(tc, 1):
    r = sol.lengthOfLongestSubstring(s)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
