# Time Complexity: O(n) - loop through the string once, and operations like `max(count.values())` are constant time because there are at most 26 characters.
# Space Complexity: O(1) - `count` only stores counts for up to 26 characters.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of counts in the current window
        count = {}
        
        left, right = 0, 0
        res = 0
        
        # move the right pointer across the string
        for right in range(len(s)):
            # update the count for the character at the right pointer
            count[s[right]] = count.get(s[right], 0) + 1

            # if the window size minus the most frequent char count is bigger than k,
            # need to shrink the window from the left
            while (right - left + 1) - max(count.values()) > k:
                # reduce the count of the char at the left pointer and move the left pointer
                count[s[left]] -= 1
                left += 1

            # update the max length of the valid window
            res = max(res, right - left + 1)

        return res
