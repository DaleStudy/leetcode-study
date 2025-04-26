/**
 * 주어진 금액을 동전으로 거스를 때 최소 동전 개수를 반환하는 함수
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
const coinChange = function (coins, amount) {
    const dp = [0, ...Array(amount).fill(amount + 1)];

    for (let coin of coins) {
        for (let n = coin; n <= amount; n++) {
            dp[n] = Math.min(dp[n], dp[n - coin] + 1)
        }
    }

    return dp[amount] > amount ? -1 : dp[amount]
};

// 시간복잡도: O(c*n) (c: coins.length, n: amount)
// 공간복잡도: O(n)
