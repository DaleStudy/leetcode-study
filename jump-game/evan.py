def canJump(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True

    for i in range(n):
        if dp[i]:
            maxJump = min(i + nums[i], n - 1)
            
            for j in range(i + 1, maxJump + 1):
                dp[j] = True

    return dp[n - 1]
