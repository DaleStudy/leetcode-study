# Time Complexity: O(N) - go through the string with two pointers, so it's basically O(N).
# Space Complexity: O(1) - only storing character frequencies (max 52 keys for a-z & A-Z), so it's effectively constant space.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # store character counts for t
        target_count = Counter(t)
        # window character count
        window_count = defaultdict(int)
        
        # start of the window
        left = 0  
        # min substring
        min_substring = ""
        # tracks how many characters match the required count
        matched_chars = 0  
        # unique characters needed
        required_chars = len(target_count)  
        
        for right, char in enumerate(s):
            # expand window by adding the rightmost character
            if char in target_count:
                window_count[char] += 1
                if window_count[char] == target_count[char]:
                    matched_chars += 1  

            # try shrinking the window if all required characters are present
            while matched_chars == required_chars:
                # update min substring if this one is shorter
                if min_substring == "" or (right - left + 1) < len(min_substring):
                    min_substring = s[left:right + 1]

                # remove leftmost character and move left pointer
                if s[left] in window_count:
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < target_count[s[left]]:
                        matched_chars -= 1
                left += 1  

        return min_substring
