class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Remove non-alphanumeric characters and convert to lowercase
        # 2. Compare with reversed string

        # cleaned_s = ""
        # for ch in s:
        #     if ch.isalnum():
        #         cleaned_s += ch.lower()

        # return cleaned_s == cleaned_s[::-1]

# Time Complexity : O(n)
# Space Complexity : O(n)

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

# Time Complexity : O(n)
# Space Complexity : O(1)
