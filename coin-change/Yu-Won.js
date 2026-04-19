/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 *
 * 문제: https://leetcode.com/problems/coin-change/
 * 요구사항: 동전과 총 금액이 주어질 때 해당 금액을 만드는데 최소 동전 개수를 반환
 */
const coinChange = (coins, amount) => {
    let dp = new Array(amount + 1).fill(amount + 1);
    dp[0] = 0;
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (i - coin >= 0) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    return dp[amount] > amount ? -1 : dp[amount];
};
