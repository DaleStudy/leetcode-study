# TC : O(n) 
# SC : O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_s = []

        for ch in s:
            if 'a' <= ch and ch <= 'z' or ('0' <= ch and ch <= '9'):
                refined_s.append(ch)
                continue

            if 'A' <= ch and ch <= 'Z':
                refined_s.append(ch.lower())
        
        for i in range(len(refined_s)):
            j = len(refined_s) - i - 1
            if refined_s[i] != refined_s[j]:
                return False
            
        return True
