def numDecodings(s: str) -> int:
    if not s:
        return 0

    n = len(s)

    # dp[i] represents the number of ways to decode the string s[:i]
    dp = [0] * (n + 1)
    dp[0] = 1

    dp[1] = 1 if s[0] != "0" else 0

    for i in range(2, n + 1):
        if s[i - 1] != "0":
            # If the one-digit number is valid, we can decode it
            dp[i] += dp[i - 1]

        two_digit = int(s[i - 2 : i])

        if 10 <= two_digit <= 26:
            # If the two-digit number is valid, we can decode it
            dp[i] += dp[i - 2]

    return dp[n]
