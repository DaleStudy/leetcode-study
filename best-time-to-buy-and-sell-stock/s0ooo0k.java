class Solution {
    public int maxProfit(int[] prices) {
        int price = prices[0];
        int maxProfit = 0;

        for(int i=1; i<prices.length; i++){
            int profit = prices[i]-price;
            maxProfit = Math.max(maxProfit, profit);
            price = Math.min(price, prices[i]);
        }
        return maxProfit;
    }
}

