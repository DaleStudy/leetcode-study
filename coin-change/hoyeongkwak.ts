function coinChange(coins: number[], amount: number): number {
    /*
    O(n)
    O(n)
    */
    if (amount === 0) return 0

    const dp = new Array(amount + 1).fill(Infinity)
    dp[0] = 0
    for(let coin of coins) {
        for (let idx = coin; idx <= amount; idx++) {
            dp[idx] = Math.min(dp[idx], dp[idx - coin] + 1)
        }
    }
    if (dp[amount] === Infinity) {
        return -1
    } else {
        return dp[amount]
    }
};
