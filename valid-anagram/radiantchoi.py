class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}

        for letter in s:
            s_letters[letter] = s_letters.get(letter, 0) + 1
        
        for letter in t:
            t_letters[letter] = t_letters.get(letter, 0) + 1

        return s_letters == t_letters 
