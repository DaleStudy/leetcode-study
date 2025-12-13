/**
 * Runtime: 1ms
 * Time Complexity: O(n)
 *
 * Memory: 94.08MB
 * Space Complexity: O(1)
 *
 * Approach: 그리디 알고리즘
 * - 주어진 prices 배열을 순회하며 최소 가격(min)을 갱신
 */
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int min = prices[0];

        for (int i=1; i<prices.length; i++) {
            if (min >= prices[i]) {
                min = prices[i];
            } else {
                maxProfit = Math.max(maxProfit, prices[i]-min);
            }
        }

        return maxProfit;
    }
}
