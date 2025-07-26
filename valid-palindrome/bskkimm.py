class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        only_al_nu = []
        
        # "2 man, a plan, a canal: Panam2"
        # 1. Delete non-alphanumeric elements and space
        for cha in s:
            if cha.isalpha() or cha.isnumeric():
                if cha.isalpha():
                    cha = cha.lower()
                only_al_nu.append(cha)
        
        # 2. extract the last and first elements and check if they are same
        while len(only_al_nu) > 1:
            if only_al_nu.pop() != only_al_nu.pop(0):
                return False

        return True
