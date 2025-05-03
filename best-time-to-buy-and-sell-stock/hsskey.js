/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy = prices[0]
    let maxVal = 0

    for(let i = 1; i < prices.length; i++) {
        if(prices[i - 1] > prices[i]) {
            buy = Math.min(buy, prices[i])
        }

        if(prices[i - 1] < prices[i]) {
            maxVal = Math.max(maxVal, prices[i] - buy)
        }
    }
    return maxVal
};
