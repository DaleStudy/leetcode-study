/**
 * 최대 수익을 구하는 알고리즘
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(1)
 * @param prices
 */
function maxProfit(prices: number[]): number {
    let min = prices[0]
    let total = 0

    for(let i = 1 ; i < prices.length ; i++) {
        min = Math.min(min, prices[i])
        // console.log(dp[i],'===', dp[i-1], '===', prices[i])
        total = Math.max(total, prices[i] - min)
    }

    return total
}
