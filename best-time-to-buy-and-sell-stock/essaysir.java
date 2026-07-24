class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        // prices = [7,1,5,3,6,4]
        int lt = 0;
        for ( int i = 1 ; i < prices.length; i ++){
            if ( prices[i] < prices[lt] ){
                lt = i;
            }
            else{
                result = Math.max(result, prices[i] - prices[lt]);
            }
        }

        return result;
    }
}
