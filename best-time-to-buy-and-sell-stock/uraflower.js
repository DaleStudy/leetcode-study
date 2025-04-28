/**
 * 주어진 prices에서 가장 큰 prices[j] - prices[i] (i < j) 를 반환하는 함수
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function(prices) {
    let min = prices[0];
    let profit = 0;
    
    for (const price of prices) {
        min = Math.min(min, price);
        profit = Math.max(profit, price - min);
    }

    return profit;
};
// 시간복잡도: O(n)
// 공간복잡도: O(1)
