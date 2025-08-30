// Time Complexity: O(n), n: prices.length
// Space Complexity: O(1), because 3 int-variables are declared -> O(1)+O(1)+O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int sellPrice = 0;
        int profit = 0;  // store maxProfit

        for (int i = 1; i < prices.length; ++i) {
            buyPrice = Math.min(buyPrice, prices[i]);
            profit = Math.max(profit, prices[i] - buyPrice);
        }

        return profit;
    }
}
