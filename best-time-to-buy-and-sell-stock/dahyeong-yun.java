/**
  * TC : O(n)
  *   - 가격 배열 n-1 만큼 순회하므로 O(n)
  * SC : O(1)
  *   - 상수 개의 변수만 사용하므로 O(1)
  */
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0; // 안사는 것이 최선인 경우
        int minPrice = prices[0]; // 첫번째 가격으로 사는 경우

        for(int i=1; i<prices.length; i++) { // 다음 날 부터 차익이 있을 수 있음.
            minPrice = Math.min(minPrice, prices[i]); // 최저가 갱신
            maxProfit = Math.max(prices[i] - minPrice, maxProfit); // 최저가 기준 오늘 팔았을 때 이익 갱신
        }
        return maxProfit;
    }
}
