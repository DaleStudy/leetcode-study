/**
 * [Problem]: [121] Best Time to Buy and Sell Stock
 *
 * (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
 */
function maxProfit(prices: number[]): number {
    //시간복잡도: O(n^2);
    //공간복잡도: O(1);
    // Time Limit Exceeded
    function doublyLoopFunc(prices: number[]): number {
        let result = 0;
        for (let i = 0; i < prices.length; i++) {
            for (let j = i + 1; j < prices.length; j++) {
                let profit = prices[j] - prices[i];
                result = Math.max(profit, result);
            }
        }

        return result;
    }

    // 시간 복잡도: O(n)
    // 공간 복잡도: O(1)
    function twoPointerFunc(prices: number[]): number {
        let minPrice = prices[0];
        let maxProfit = 0;

        for (let i = 1; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            } else {
                maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            }
        }

        return maxProfit;
    }

    return twoPointerFunc(prices);
}
