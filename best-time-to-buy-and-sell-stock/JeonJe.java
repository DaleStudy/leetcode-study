import java.util.*;

// TC: O(n)
// SC: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxProfit = 0;
        int minPrice = prices[0];

        for (int sellDay = 1; sellDay < n; sellDay++) {
            minPrice = Math.min(minPrice, prices[sellDay]);
            maxProfit = Math.max(maxProfit, prices[sellDay] - minPrice);
        }

        return maxProfit;
    }
}
