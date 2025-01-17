class Solution {
    public int maxProfit(int[] prices) {
        /**
        1. understanding
        - price[i]: i th day's stock price
        - to maximize profit, choose a single day to buy, and future day to sell.
        - return maximum profit
        - [7, 1, 5, 3, 6, 4] -> [0, 0, 4, 4, 5, 5]
        - [7, 6, 4, 3, 1] -> [0, 0, 0, 0, 0]
        2. strategy
        - profit = (sell price) - (buy price)
        3. complexity
        - time: O(N)
        - space: O(1)
        */
        int minPrice = prices[0];
        for (int i = 0; i <prices.length; i++) {
            int tmp = prices[i];
            if (i == 0) {
                prices[i] = 0;
            } else {
                prices[i] = Math.max(prices[i-1], prices[i] - minPrice);
            }
            minPrice = Math.min(minPrice, tmp);
        }

        return prices[prices.length - 1];
    }
}

