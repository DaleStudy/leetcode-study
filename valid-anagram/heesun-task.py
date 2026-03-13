# Leetcode 242. Valid Anagram
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(k)
    def isAnagram(self, s: str, t: str) -> bool:
        # base case:
        if len(s) != len(t):
            return False

        # create a dictionary that counts the number of each letter in s
        s_dict = {}
        for s_letter in s:
            if s_letter in s_dict:
                s_dict[s_letter] += 1
            else:
                s_dict[s_letter] = 1

        # loop the dictionary and match with the number of t
        for t_letter in t:
            if t_letter not in s_dict:
                return False
            else:
                s_dict[t_letter] -= 1
                if s_dict[t_letter] == 0:
                    del s_dict[t_letter]

        return len(s_dict) == 0