/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxGap = 0;

    for(let i =0; i < prices.length; i++){
        const price = prices[i];
        const restList = prices.slice(i);

        const max = Math.max(...restList);

        maxGap = Math.max(max-price, maxGap)
    }

    return maxGap
};

