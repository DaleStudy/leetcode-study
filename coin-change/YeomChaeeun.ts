/**
 * 동전들로 금액을 만들때 필요한 최소 동전의 개수 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(nxm) 동전의 개수 x 만들어야하는 금액의 크기
 * - 공간 복잡도: O(m) 주어진 금액에 비례함
 * @param coins
 * @param amount
 */
function coinChange(coins: number[], amount: number): number {
    const dp = new Array(amount + 1).fill(amount + 1)
    dp[0] = 0 // 0원은 0개

    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1)
        }
    }

    return dp[amount] === amount + 1 ? -1 : dp[amount]
}
