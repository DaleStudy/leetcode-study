package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `best-time-to-buy-and-sell-stock` {

    fun maxProfit(prices: IntArray): Int {
        if (prices.size == 1) return 0
        return usingKadaneAlgorithm(prices)
    }

    /**
     * 1. 방향이 존재하기 때문에 투 포인터를 활용하여 주식을 팔 수 있는 경우라면 최대 값을 계산하고 만약 산 가격보다 싼 가격을 만나면 다시 산다
     * TC: O(n), SC: O(1)
     */
    private fun usingTwoPointer(prices: IntArray): Int {
        var (left, right) = 0 to 1
        var maxProfit = 0

        while (right < prices.size) {
            if (prices[left] < prices[right]) {
                maxProfit = max(prices[right] - prices[left], maxProfit)
                right++
            } else if (prices[left] >= prices[right]) {
                left = right
                right++
            }
        }

        return maxProfit
    }

    /**
     * 2. 카데인 알고리즘의 변형된 버전으로 가장 싼 경우를 buy에 저장하고 현재 최대 수익을 초과하면 업데이트한다
     * TC: O(n), SC: O(1)
     */
    private fun usingKadaneAlgorithm(prices: IntArray): Int {
        var buy = prices[0]
        var maxProfit = 0

        for (index in 1 until prices.size) {
            if (prices[index] < buy) {
                buy = prices[index]
            } else if (prices[index] - buy > maxProfit) {
                maxProfit = prices[index] - buy
            }
        }
        return maxProfit
    }

    @Test
    fun `주어진 가격 배열을 통해 최대의 수익을 반환한다`() {
        maxProfit(intArrayOf(3,3)) shouldBe 0
        maxProfit(intArrayOf(7,6,5,4,3,2,1,0)) shouldBe 0
        maxProfit(intArrayOf(7,1,5,3,6,4)) shouldBe 5
        maxProfit(intArrayOf(1,2,4,2,5,7,2,4,9,0,9)) shouldBe 9
    }
}
