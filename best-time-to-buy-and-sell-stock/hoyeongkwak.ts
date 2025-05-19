/* 
    time complexity : O(n)
    space complexity : O(1)
*/
function maxProfit(prices: number[]): number {
    let left = 0
    let right = 0
    let maxProfit = 0

    while (right < prices.length) {
        const curProfit = prices[right] - prices[left]
        if (prices[left] < prices[right]) {
            maxProfit = Math.max(curProfit, maxProfit)
        } else {
            left = right
        }
        right += 1
    }
    return maxProfit
};
