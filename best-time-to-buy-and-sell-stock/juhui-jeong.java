/*
시간복잡도: O(n²)
공간복잡도: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int maxStock = 0;
        for(int i = 0; i < prices.length; i++) {
            for (int j = 0; j < prices.length; j++) {
                if (i <= j) break;
                if (prices[i] - prices[j] > maxStock) {
                    maxStock = prices[i] - prices[j];
                }
            }
        }
        return maxStock;
    }
}
 */
// 시간복잡도: O(n)
// 공간복잡도: O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int maxStock = 0;
        int minPrice = prices[0];
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else {
                maxStock = Math.max(price - minPrice, maxStock);
            }
        }
        return maxStock;
    }
}
