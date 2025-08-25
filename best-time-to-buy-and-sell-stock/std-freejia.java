/** 
 * 121. Best Time to Buy and Sell Stock
 * 반복문 돌면서 가장 작은 값을 기억해둡니다 
 * 매번 최소값과의 차이를 비교합니다 
 */
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;

        for (int price: prices) {
            if (price < minPrice) { // 최소 값 찾기
                minPrice = price;
            }
            if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice;
            }
        }
        return maxProfit;
    }
}
