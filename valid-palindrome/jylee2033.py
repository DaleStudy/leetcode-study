class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Remove non-alphanumeric characters and convert to lowercase
        # 2. Compare with reversed string

        cleaned_s = ""
        for ch in s:
            if ch.isalnum():
                cleaned_s += ch.lower()

        return cleaned_s == cleaned_s[::-1]

# Time Complexity : O(n)
# Space Complexity : O(n)
