class Solution {
  /**
   시간복잡도: O(n)
   공간복잡도: O(1)
   */
  public int maxProfit(int[] prices) {
    int buyPrice = prices[0];
    int maxProfit = 0;

    for(int i = 0; i < prices.length; i++) {
      buyPrice = Math.min(buyPrice, prices[i]);
      maxProfit = Math.max(maxProfit, prices[i] - buyPrice);
    }

    return maxProfit;
  }
}
