class Solution {
    /**
     * 오늘 주식을 판매한다고 가정하면,
     * 이전 날짜 중 가장 낮은 가격에 구매했을 때 최대 이익을 얻을 수 있다.
     * 배열을 순회하면서 최저 가격과 최대 이익을 계속 갱신한다.
     *
     * 시간 복잡도: O(n)
     * 공간 복잡도: O(1)
     */
    public int maxProfit(int[] prices) {
        // 현재까지 확인한 날짜 중 가장 낮은 주가
        int minPrice = prices[0];

        // 현재까지 얻을 수 있는 최대 이익
        int maxProfit = 0;

        // 첫 번째 가격은 minPrice로 사용했으므로 두 번째 가격부터 확인한다.
        for (int i = 1; i < prices.length; i++) {
            int currentPrice = prices[i];
            int currentProfit = currentPrice - minPrice;

            // 이전 최저가에 구매하고 현재 가격에 판매했을 때의 이익을 비교한다.
            maxProfit = Math.max(maxProfit, currentProfit);

            // 이후 날짜의 계산을 위해 지금까지의 최저가를 갱신한다.
            minPrice = Math.min(minPrice, currentPrice);
        }

        return maxProfit;
    }
}
