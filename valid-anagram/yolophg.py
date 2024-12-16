# Time Complexity: O(n)  
# Go through both strings once to count and compare characters.

# Space Complexity: O(1)  
# The dictionary stores at most 26 letters, so space usage is constant.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        
        # count frequencies of characters in string s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # go through 't' and decrease the count
        for char in t:
            # if the character isn't in the dictionary, it's not an anagram
            if char in char_count:
                char_count[char] -= 1
            else:
                return False

        # check if all the counts are zero
        for val in char_count.values():
            if val != 0:
                return False
        
        return True
