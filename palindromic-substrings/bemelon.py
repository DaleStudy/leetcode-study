class Solution:
    def countSubstrings_v1(self, s: str) -> int:
        def isPalindrome(self, substr: str) -> bool:
            return len(substr) <= 1 or (substr[0] == substr[-1] and self.isPalindrome(substr[1:-1]))

        # Brute-Force Solution - TLE 
        count = 0
        for l in range(1, len(s) + 1):
            for start in range(0, len(s)):
                if start + l > len(s): continue 

                substr = s[start: start + l]
                if (self.isPalindrome(substr)):
                    count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        """
        Dynamic Programming Solution
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        """
        n = len(s)

        # isPalindrome[i][j] => Palindrome at s[i:j]?
        isPalindrome = [[False] * n for _ in range(n)] 
        answer = 0
        # 1. "a", "b", "c" are all Palindrome 
        for i in range(n):
            isPalindrome[i][i] = True 
            answer += 1

        # 2. "a{x}" are Palindrome if a == {x} 
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True 
                answer += 1
        
        # 3. else) str[i:j] is Palindrome if str[i + 1: j - 1] ... is Palinedrome 
        for size in range(3, n + 1):
            for start in range(n - size + 1): 
                end = start + size - 1

                if s[start] == s[end] and isPalindrome[start + 1][end - 1]: 
                    isPalindrome[start][end] = True
                    answer += 1

        return answer

