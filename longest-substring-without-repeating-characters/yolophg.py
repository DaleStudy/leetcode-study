# Time Complexity: O(n): both pointers (left and right) traverse the string once.
# Space Complexity: O(n): worst case, all characters are unique, so the set will store all characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # to store characters in the current window
        window_set = set()  
        # to store the max length of a substring
        max_length = 0  
        # left pointer for the sliding window
        left = 0  

        # iterate through each char in the string using the right pointer
        for right in range(len(s)):
            # if the char is already in the window, shrink the window
            while s[right] in window_set:
                window_set.remove(s[left])  # remove the leftmost char
                left += 1  # move the left pointer to the right
            # add the new char
            window_set.add(s[right])
            # update the max length if the current window is longer
            max_length = max(max_length, right - left + 1)

        return max_length
