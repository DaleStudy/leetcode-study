class Solution {
    public int maxProfit(int[] prices) {
        /**
        1. 하루에 팔아서 가장 최대 이익을 구하도록하는 max price return
        2. 조건
        - 미래 다른날짜에 판매 (이전 날짜에 판매 x)
        - choosing a single day
        - 배열 길이 min = 1, max = 10^5
        - 원소값 : min = 0, max = 10^4
        3. 풀이
        - 1)brtueforce: time complexity O(n^2), space: O(1)
        - 2)현재 값 - 이전 값 중 가장 최소값 -> maxProfit , 즉 min값을 계속 기억하다가 현재 값과의 차이 중 가장 큰 값을 구하면된다.
        - time: O(n)
        - space: O(1)
         */

        int maxProfit = 0;
        int minStock = Integer.MAX_VALUE;
        int n = prices.length;

        for(int i = 0; i<n; i++) {
            if(prices[i] < minStock) {
                minStock = prices[i];
            }
            if(i > 0 && prices[i] - minStock > maxProfit) {
                maxProfit = Math.max(maxProfit, prices[i] - minStock);
            }
        }
        return maxProfit;


        // for(int i = 0; i < n; i++) {
        //     int curStock = prices[i];
        //     for(int j= i + 1; j < n; j++) {
        //         if(curStock < prices[j]) {
        //             int curProfit = prices[j] - curStock;
        //             maxProfit = Math.max(maxProfit, curProfit);
        //         }
        //     }
        // }
        // return maxProfit;
    }
}
