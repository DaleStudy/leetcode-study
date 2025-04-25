/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0; // 0원을 만들기 위한 동전 수는 0개

    // bottom-up DP
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (i - coin >= 0) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    return dp[amount] === Infinity ? -1 : dp[amount];
};

// 시간복잡도: O(amount * coins.length)
// -> 각 금액 i마다 모든 coin을 시도하기 때문
// 공간복잡도: O(amount)
// -> dp 배열을 사용하기 때문
