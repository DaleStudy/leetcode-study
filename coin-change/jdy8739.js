/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = [0, ...(new Array(amount).fill(amount + 1))];

    for (coin of coins) {
        for (let a = coin; a <= amount; a++) {
            dp[a] = Math.min(dp[a], dp[a - coin] + 1);
        }
    }

    return dp[amount] < amount + 1 ? dp[amount] : -1
};