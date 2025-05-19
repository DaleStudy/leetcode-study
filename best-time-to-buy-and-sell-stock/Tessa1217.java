/**
 * 주식 가격이 주어지는 prices 배열이 있을 때 최대 주식 이익을 구하시오
 * 주식을 산 날짜에는 팔 수 없으며 반드시 산 날짜의 이후 날짜부터(미래부터) 팔 수 있다.
 */
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int min = prices[0];
        // 굳이 DP 배열 쓰지 않고 계산, 공간 복잡도 낮추기
        for (int i = 0; i < prices.length; i++) {
            int profit = prices[i] - min;
            maxProfit = Math.max(profit, maxProfit);
            min = Math.min(prices[i], min);
        }
        return maxProfit;
    }

    // public int maxProfit(int[] prices) {
    //     // 최저 구매
    //     int[] dp = new int[prices.length];
    //     dp[0] = prices[0];
    //     for (int i = 1; i < prices.length; i++) {
    //         dp[i] = Math.min(prices[i], dp[i - 1]);            
    //     }
    //     // 최저 구매 배열 기준으로 당일 최대 이익 계산
    //     int profit = 0;
    //     for (int i = 1; i < prices.length; i++) {
    //         profit = Math.max(prices[i] - dp[i - 1], profit);
    //     }
    //     return profit;
    // }
}

