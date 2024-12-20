# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up the string: remove non-alphanumeric chars and convert to lowercase
        # isalnum() checks if the character is alphanumeric
        filtered = ''.join(filter(str.isalnum, s)).lower()
        
        # check if it reads the same forwards and backwards
        # filtered[::-1] flips the string
        return filtered == filtered[::-1]
