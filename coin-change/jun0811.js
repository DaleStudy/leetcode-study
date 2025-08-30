var coinChange = function(coins, amount) {
    if(amount == 0) return 0

    const dp = [0, ...new Array(amount).fill(amount+1)]

    for (const coin of coins) {
        for (let i = coin; i <=amount; i++) {
            dp[i] = Math.min(dp[i], dp[i-coin] + 1)
        }
    }

    return dp[amount] < amount+1 ? dp[amount] : -1
};
