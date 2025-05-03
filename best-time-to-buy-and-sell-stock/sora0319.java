class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        for(int p : prices){
            if(minPrice < p && maxProfit < p - minPrice){
                maxProfit = p - minPrice;
            }
            if(minPrice > p){
                minPrice = p;
            }
        }
        return maxProfit;
    }
}

