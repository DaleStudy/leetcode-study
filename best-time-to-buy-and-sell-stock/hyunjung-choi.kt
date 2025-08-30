/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var minPrice = Int.MAX_VALUE
        var maxProfit = 0

        prices.forEach { price ->
            minPrice = minOf(minPrice, price)
            maxProfit = maxOf(maxProfit, price - minPrice)
        }

        return maxProfit
    }
}
