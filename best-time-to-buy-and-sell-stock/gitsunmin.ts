/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock
 * time complexity : O(n)
 * space complexity : O(1)
 */

function maxProfit(prices: number[]): number {
    let maxProfit = 0;
    let [minPrice] = prices;

    for (let price of prices) {
        maxProfit = Math.max(maxProfit, price - minPrice);
        minPrice = Math.min(minPrice, price);
    }

    return maxProfit;
};
