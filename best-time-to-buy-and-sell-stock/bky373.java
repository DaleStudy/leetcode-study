/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 * TC : O(N)
 * SC : O(1)
 */
class Solution_0121 {
    public int maxProfit(int[] prices) {
        int hold = prices[0];
        int profit = 0;

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] < hold) {
                hold = prices[i];
            }

            if (prices[i] - hold > profit) {
                profit = prices[i] - hold;
            }
        }
        return profit;
    }
}
