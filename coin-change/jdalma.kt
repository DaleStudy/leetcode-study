package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.util.ArrayDeque
import kotlin.math.min

class `coin-change` {

    fun coinChange(coins: IntArray, amount: Int): Int {
        return topDown(coins, amount)
    }

    /**
     * 1. 모든 코인을 반복적으로 사용하면서 0원에 도달하면 그 때의 step 중 최솟값을 반환한다.
     * TC: O(coins^amount), SC: O(amount)
     */
    private fun bruteForce(coins: IntArray, amount: Int): Int {
        fun dfs(coins: IntArray, remain: Int, step: Int): Int =
            if (remain < 0) Int.MAX_VALUE
            else if (remain == 0) step
            else coins.map { dfs(coins, remain - it, step + 1) }.min()

        val result = dfs(coins, amount, 0)
        return if (result == Int.MAX_VALUE) -1 else result
    }

    /**
     * 2. 모든 코인들을 종류별로 누적하면서 가장 빨리 목푯값에 도달하는 코인의 수를 반환한다.
     * TC: O(amount * coins), SC: O(amount)
     */
    private fun bfs(coins: IntArray, amount: Int): Int {
        if (amount == 0) return 0

        val visited = BooleanArray(amount + 1) { false }
        val queue = ArrayDeque<Int>().apply {
            this.offer(0)
        }

        var coinCount = 0
        while (queue.isNotEmpty()) {
            var size = queue.size
            while (size-- > 0) {
                val sum = queue.poll()
                if (sum == amount) return coinCount
                else if (sum < amount && !visited[sum] ) {
                    visited[sum] = true
                    for (coin in coins) {
                        queue.offer(sum + coin)
                    }
                }
            }
            coinCount++
        }
        return -1
    }

    /**
     * 3. 반복되는 연산을 DP를 활용하여 bottom-up으로 해결
     * 1원부터 목푯값까지 각 가치를 구성하기 위한 최소 코인을 누적하면서 목푯값을 구성하는 최소 코인 개수를 구하는 것이다.
     * TC: O(amount*coins), SC: O(amount)
     */
    private fun bottomUp(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount + 1) { 10000 + 1 }.apply {
            this[0] = 0
        }

        for (target in 1 .. amount) {
            coins.forEach {  coin ->
                if (coin <= target) {
                    dp[target] = min(dp[target], dp[target - coin] + 1)
                }
            }
        }

        return if (dp[amount] == 10001) -1 else dp[amount]
    }

    /**
     * 4. 목표금액부터 코인만큼 차감하여 0원에 도달하면 백트래킹으로 DP 배열을 갱신한다
     * TC: O(amount * coins), SC: O(amount)
     */
    private fun topDown(coins: IntArray, amount: Int): Int {
        fun recursive(coins: IntArray, remain: Int, dp: IntArray): Int {
            if (remain == 0) return 0
            else if (remain < 0) return -1
            else if (dp[remain] != 10001) return dp[remain]

            var minCoins = 10001
            coins.forEach { coin ->
                val result = recursive(coins, remain - coin, dp)
                if (result in 0 until minCoins) {
                    minCoins = result + 1
                }
            }
            dp[remain] = if (minCoins == 10001) -1 else minCoins
            return dp[remain]
        }

        if (amount < 1) return 0
        return recursive(coins, amount, IntArray(amount + 1) { 10000 + 1 })
    }

    @Test
    fun `코인의 종류와 목표값을 입력하면 목푯값을 구성하는 코인의 최소 개수를 반환한다`() {
        coinChange(intArrayOf(1,2,5), 11) shouldBe 3
        coinChange(intArrayOf(1,3,5), 15) shouldBe 3
        coinChange(intArrayOf(5,3,1), 15) shouldBe 3
        coinChange(intArrayOf(1,2), 4) shouldBe 2
        coinChange(intArrayOf(2,5,10,1), 27) shouldBe 4
    }

    @Test
    fun `코인의 종류로 목표값을 완성할 수 없다면 -1을 반환한다`() {
        coinChange(intArrayOf(2), 3) shouldBe -1
    }

    @Test
    fun `목푯값이 0이라면 0을 반환한다`() {
        coinChange(intArrayOf(1,2,3), 0) shouldBe 0
    }
}
