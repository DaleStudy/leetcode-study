"""
91. Decode Ways
https://leetcode.com/problems/decode-ways/

Solution: Dynamic Programming
    We can use dynamic programming to count the number of ways to decode the input string.
    We can define a dp array to store the number of ways to decode the string up to the current index.
    We can iterate through the input string and update the dp array based on the current character and the previous characters.
    The number of ways to decode the string up to the current index is the sum of the number of ways to decode the previous two characters.
    
    - Initialize a dp array with length n + 1 and set dp[0] to 1.
    - Iterate through the input string starting from the first character.
        - Update dp[i] based on the current character and the previous characters.
    - Return dp[n].

Time complexity: O(n)
    - We iterate through the input string once.

Space complexity: O(n)
    - We use a dp array of length n + 1 to store the number of ways to decode the string up to each index.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i > 1 and "10" <= s[i - 2 : i] <= "26":
                dp[i] += dp[i - 2]

        return dp[n]
