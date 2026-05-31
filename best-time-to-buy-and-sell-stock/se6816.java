
/**
    dp를 이용한 방식?
    prices의 길이 -> N
    시간복잡도 : O(N^2) -> 시간 초과
    공간복잡도 : O(N)
 */
class Solution2 {
    public int maxProfit(int[] prices) {
        int[] dp =new int[prices.length];
        for(int i = 0; i < dp.length; i++) {
            for(int j = 0; j < i; j++) {
                dp[i] = Math.max(dp[i], prices[i] - prices[j]);
            }
        }
    
        return Arrays.stream(dp)
                    .max()
                    .getAsInt();
    }
}

/**
    이전 연산 값을 기억할 필요 없이 특정 인덱스 지점까지의 최소 값만 알면 되므로,

    prices의 길이 -> N
    시간복잡도 : O(N) 
    공간복잡도 : O(1)
 */
class Solution {
    public int maxProfit(int[] prices) {
        int min=prices[0];
        int profit=0;
        for(int i=1; i<prices.length; i++){
            if(prices[i] < min){
                min=prices[i];
                continue;
            }
            profit=Math.max(profit, prices[i] - min);
        }
        return profit;
    }
}
