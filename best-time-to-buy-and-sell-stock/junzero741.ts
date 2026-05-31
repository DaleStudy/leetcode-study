// TC: O(N)
// SC: O(1)
function maxProfit(prices: number[]): number {
    let maxProfit = 0
    let minPrice = Infinity

    for(const price of prices) {
        maxProfit = Math.max(price - minPrice, maxProfit)
        minPrice = Math.min(price, minPrice)
    }

    return maxProfit
    
};

