"""
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
- Use a defaultdict to track the count of each character in the current window.
- Maintain two pointers, 'left' and 'right', to represent the sliding window over the string.
- As we iterate over the string with 'right', increment the count for the current character.
- If a duplicate character appears in the window (count > 1), move the 'left' pointer forward and decrement counts until there are no duplicates.
- After adjusting, update 'ans' with the maximum length found for a window with all unique characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        ans = left = 0

        for right, val in enumerate(s):
            count[val] += 1

            while count[val] > 1:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
