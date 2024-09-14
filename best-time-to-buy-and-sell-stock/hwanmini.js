// 시간복잡도: O(n)
// 공간복잡도: O(1)
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (!prices || !prices.length) return 0

    let maxBenefit = 0;
    let buyPrice = Infinity;

    for (let i = 0 ; i < prices.length ; i++) {
        buyPrice = Math.min(buyPrice, prices[i]);
        maxBenefit = Math.max(maxBenefit, prices[i] - buyPrice)
    }


    return maxBenefit
};

console.log(maxProfit([7,1,5,3,6,4]))
console.log(maxProfit([7,6,4,3,1]))
