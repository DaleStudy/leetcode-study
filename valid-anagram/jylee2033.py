class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Build a hashmap counting characters in t
        char_count = {}

        # for letter in t:
        #     if letter not in char_count:
        #         char_count[letter] = 1
        #     else:
        #         char_count[letter] += 1

        for letter in t:
            char_count[letter] = char_count.get(letter, 0) + 1

        # Decrease counts using characters from s
        for letter in s:
            if letter not in char_count:
                return False

            char_count[letter] -= 1

            # If count becomes negative, s has extra characters
            if char_count[letter] < 0:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(1) since the hashmap stores at most 26 letters
