/**

 최대이익 = 최고금액 - 최소금액
 */
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maximumProfit = 0;

        for(int price : prices) {
            if(price < minPrice) {
                minPrice = price;
            }
            int currentProfit = price - minPrice;
            if(currentProfit > maximumProfit) {
                maximumProfit = currentProfit;
            }
        }
        return maximumProfit;
    }
}

