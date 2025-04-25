class Solution:
    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(n)
    """
    def numDecodingsDP(self, s: str) -> int:
        if s[0] == "0":
            return 0
                
        n = len(s)
        dp = [0] * (n + 1)
        # dp[0] => empty string => 1 case
        # dp[1] => not 0 => 1 case (single digit)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1:i])
            two_digit = int(s[i - 2:i])

            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]

    """
        - Time Complexity: O(n), n = len(s)
        - Space Complexity: O(1)
    """
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        # Using two variables for checking single and double digit
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current += prev1
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                current += prev2
            prev2, prev1 = prev1, current
        
        return prev1    # prev1 = current
    
tc = [
        ("12", 2),
        ("226", 3),
        ("06", 0)
]

for i, (s, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.numDecodings(s)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
