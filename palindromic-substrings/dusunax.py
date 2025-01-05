'''
# 647. Palindromic Substrings

A. use dynamic programming table to store the palindrome status.
B. use two pointers to expand around the center.

## Time and Space Complexity

### A. Dynamic Programming Table
```
TC: O(n^2)
SC: O(n^2)
```

#### TC is O(n^2):
- filling DP table by iterating through all substrings. 
- each cell (i, j) checks if a substring is a palindrome & counting the cases = O(n^2)

#### SC is O(n^2):
- storing the n x n dp table. = O(n^2)

### B. Expand Around Center
```
TC: O(n^2)
SC: O(1)
```

#### TC is O(n^2):
- for each char, expand outwards to check for palindromes. = O(n^2)

#### SC is O(1):
- no additional data structures are used. `count` is a single integer. = O(1)
'''
class Solution:
    def countSubstringsDPTable(self, s: str) -> int:
        '''
        A. Dynamic Programming Table
        '''
        n = len(s)
        dp = [[False] * n for _ in range(n)] # List comprehension. = SC: O(n^2)
        count = 0

        for i in range(n): # TC: O(n)
            dp[i][i] = True
            count += 1
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        for s_len in range(3, n + 1): # TC: O(n)
            for i in range(n - s_len + 1): # TC: O(n) 
                j = i + s_len - 1
                
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count
    def countSubstrings(self, s: str) -> int:
        '''
        B. Expand Around Center
        '''
        count = 0

        def expand(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]: # TC: O(n)
                count += 1
                left -= 1
                right += 1
        
        for i in range(len(s)): # TC: O(n)
            expand(i, i)
            expand(i, i + 1)
        
        return count
