/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number} 
 */
var coinChange = function (coins, amount) {

    let dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;

    for (let i = 1; i < dp.length; i++) {
        for (let coin of coins) {

            if (coin > i) {
                continue;
            }

            let remain = i - coin;
            dp[i] = Math.min(dp[i], dp[remain] + 1);

        }
    };

    let result = dp[amount] === Infinity ? -1 : dp[amount];
    return result;
}
