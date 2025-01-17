class Solution {
    /**
     * 시간 : O(n) 공간 : O(1)
     * 풀이
     *  lastIndex - 1부터 0까지 조회하면서 가장높은값(maxPrice) 에서 현재값(price[i])의 차(currentProfit)를 구한다.
     *  profit 과 currentProfit중 더 높은값이 profit.
     *  maxPrice와 prices[i]중 더 높은값이 maxPrice가 된다.
     * */
    fun maxProfit(prices: IntArray): Int {
        var profit = 0
        var maxPrice = prices[prices.lastIndex]
        for (i in prices.lastIndex - 1 downTo 0) {
            val currentProfit = maxPrice - prices[i]
            profit = max(profit, currentProfit)
            maxPrice = max(maxPrice, prices[i])
        }

        return profit
    }
}
