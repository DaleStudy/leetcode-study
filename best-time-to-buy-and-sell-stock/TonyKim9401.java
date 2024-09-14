// TC: O(n)
// SC: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int bestProfit = 0;
        int buyPrice = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (buyPrice > prices[i]) {
                buyPrice = prices[i];
                continue;
            }
            bestProfit = Math.max(bestProfit, prices[i] - buyPrice);
        }
        return bestProfit;
    }
}
