class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = ''.join(filter(str.isalnum, s)).lower()
        if not (s and s.strip()): return True 
        
        head = 0
        tail = len(s) -1
        while head < tail:
            if s[head] != s[tail]:
                return False
            else: 
                head += 1
                tail -= 1
        
        return True        
