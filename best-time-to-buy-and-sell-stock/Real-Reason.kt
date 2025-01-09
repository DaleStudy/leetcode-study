package leetcode_study

import kotlin.math.max
import kotlin.math.min
fun maxProfit(prices: IntArray): Int {
    var minPrice = prices[0]
    var maxProfit = 0

    for (i in 0 until prices.size) {
        maxProfit = max(maxProfit, prices[i] - minPrice)
        minPrice = min(minPrice, prices[i])
    }

    return maxProfit
}
