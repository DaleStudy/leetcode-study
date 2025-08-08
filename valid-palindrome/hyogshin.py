class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = []
        is_pal = True
        for c in s:
            if c.isalnum():
                alnum.append(c.lower())
        
        for c in range(len(alnum) // 2):
            if alnum[c] != alnum[-1 - c]:
                is_pal = False
                break
        
        return is_pal