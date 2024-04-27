class Solution {
    /**
     * 전체 prices 배열을 순회하므로 시간복잡도 : O(n)
     * profit은 1개의 값을 저장하므로 공간복잡도 : O(1)
     *
     * 문제를 푸는 접근이 어려워서 1시간이 넘게 소요되었다...
     * @param prices
     * @return
     */
    public int maxProfit(int[] prices) {
        // 처음 가격을 담아주고
        int buyPrice = prices[0];
        // 다음에 더 저렴한 가격이 있다면 해당 가격으로 담아준다.
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            // 현재가격
            int currentPrice = prices[i];

            if (currentPrice < buyPrice) {
                buyPrice = currentPrice;
            }

            // 현재가격과 - 내가산가격 = 이익(profit)
            if (currentPrice - buyPrice > profit) {
                profit = currentPrice - buyPrice;
            }
        }

        return profit;
    }
}
