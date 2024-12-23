class Solution(object):
    def isAnagram(self, s, t):
        character1 = []
        character2 = []

        # put characters in character1 and character2
        for i in s:
            character1.append(i)
        for i in t:
            character2.append(i)

        # sort out the characters in alphabetical order
        character1.sort()
        character2.sort()

        # compare each characters to see if they match (= anagram)
        if character1 == character2:
            return True
        else:
            return False
