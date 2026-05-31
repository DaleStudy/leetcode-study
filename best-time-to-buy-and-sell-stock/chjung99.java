class Solution {
    public int maxProfit(int[] prices) {
        int N = prices.length;
        int[] rangeMaxAfter = new int[N];
        int maxValue = prices[N-1];

        for (int i = N-1; i >= 0; i--){
            if (maxValue < prices[i]){
                maxValue = prices[i];
            }
            rangeMaxAfter[i] = maxValue;
        }

        int answer = rangeMaxAfter[0] - prices[0];

        for (int i = 0; i < N; i++){
            answer = Math.max(answer, rangeMaxAfter[i] - prices[i]);
        }

        return answer;
    }
}

