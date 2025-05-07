// NOTE: tc --> O(n)
class Solution {
    public int maxProfit(int[] prices) {

        int curMax = 0;
        int gMax = 0;

        if(prices.length == 0) return 0;
        
        int sell = prices[0];
        for(int i = 1; i < prices.length; i++) {
            curMax = Math.max(0, prices[i] - sell);

            // NOTE: 새롭게 시작하는게 더 좋은경우
            if(curMax == 0) {
                sell = prices[i];
            }

            gMax = Math.max(curMax, gMax); 
        }

        return gMax;        
    }
}
