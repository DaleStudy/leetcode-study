- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- time complexity : O(n)
- space complexity : O(1)
- https://algorithm.jonghoonpark.com/2024/02/20/leetcode-121

```java
class Solution {
    public int maxProfit(int[] prices) {
        int buyAt = 0;
        int profit = 0;

        for(int i = 1; i < prices.length; i++) {
            if (prices[i] < prices[buyAt]) {
                buyAt = i;
            } else {
                profit = Math.max(profit, prices[i] - prices[buyAt]);
            }
        }

        return profit;
    }
}
```
