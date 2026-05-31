class Solution {
    // TC : O(n)
    // SC : O(1)
    public int maxProfit(int[] prices) {
        int maximumProfit = 0;
        int cursor = 0;

        // 전체를 순회하면서 이익을 검증
        for(int i = 0; i < prices.length; i++){
            int profit = prices[i] - prices[cursor];

            // 만약 현재 값이 커서의 값보다 더 작다면 현재 값부터 비교하기 시작
            if(profit < 0){
                cursor = i;
                continue;
            }

            // 이전에 커서로 추정한 값이 높더라도 Math.max로 보존됨
            maximumProfit = Math.max(profit, maximumProfit);
        }

        return maximumProfit;
    }
}
