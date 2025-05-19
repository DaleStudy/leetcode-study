/**
 * <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">week05-1.best-time-to-buy-and-sell-stock</a>
 * <li>Description: Return the maximum profit you can achieve from this transaction</li>
 * <li>Topics: Array, Dynamic Programming       </li>
 * <li>Time Complexity: O(N), Runtime 2ms       </li>
 * <li>Space Complexity: O(1), Memory 61.62MB   </li>
 */
class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int profit = 0;
        for(int i=1; i<prices.length; i++) {
            profit = Math.max(profit, prices[i]-min);
            min = Math.min(min, prices[i]);
        }
        return profit;
    }
}
