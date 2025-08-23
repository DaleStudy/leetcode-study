function maxProfit(prices: number[]): number {

        let minPrice: number = prices[0];
        let maxProfit: number = 0;

        for (let i = 1; i < prices.length; i++) {
    // 1. compare the number later than now
            if (prices[i] < minPrice) {
    // 2. if there's bigger number later, set it as the standard
                minPrice = prices[i];
            } else {
                maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            }
        }
        return maxProfit;
};
