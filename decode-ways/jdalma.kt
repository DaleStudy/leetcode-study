package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `decode-ways` {

    fun numDecodings(s: String): Int {
        return usingOptimizedDP(s)
    }

    /**
     * 1. 문자열의 첫 인덱스부터 DFS로 확인하면서 결과를 증가시킨다. → 시간초과
     * 0부터 시작하는 문자열은 존재하지 않기에 바로 0으로 반환하고 그 뒤 숫자부터 DFS를 연이어 실행한다.
     * 시간복잡도: O(2^n), 공간복잡도: O(n)
     */
    private fun usingDfs(s: String): Int {
        fun dfs(index: Int): Int =
            if (index == s.length) 1
            else if (s[index] == '0') 0
            else if (index + 1 < s.length && (s[index] == '1' || (s[index] == '2' && s[index + 1] < '7')) )
                dfs(index + 1) + dfs(index + 2)
            else dfs(index + 1)

        return dfs(0)
    }

    /**
     * 2. 1번 풀이에서 중복되는 연산에 top-down 방향으로 메모이제이션 적용
     * 시간복잡도: O(n), 공간복잡도: O(n)
     */
    private fun usingMemoization(s: String): Int {
        fun dfs(index: Int, mem: IntArray): Int {
            println(index)
            mem[index] = if (index == s.length) 1
            else if (s[index] == '0') 0
            else if (mem[index] != 0) mem[index]
            else if (index + 1 < s.length && (s[index] == '1' || (s[index] == '2' && s[index + 1] < '7')) )
                dfs(index + 1, mem) + dfs(index + 2, mem)
            else dfs(index + 1, mem)

            return mem[index]
        }
        return dfs(0, IntArray(s.length + 1) { 0 })
    }

    /**
     * 3. 마지막 숫자부터 bottom-up 방향 DP
     * 시간복잡도: O(n), 공간복잡도: O(n)
     */
    private fun usingDP(s: String): Int {
        val dp = IntArray(s.length + 1).apply {
            this[s.length] = 1
        }

        (s.length - 1 downTo 0).forEach { index ->
            if (s[index] == '0') dp[index] = 0
            else if(index + 1 < s.length && (s[index] == '1' || (s[index] == '2' && s[index + 1] < '7')))
                dp[index] = dp[index + 1] + dp[index + 2]
            else dp[index] = dp[index + 1]
        }

        return dp[0]
    }

    /**
     * 4. 배열을 사용하지 않고 DP 적용
     * 시간복잡도: O(n), 공간복잡도: O(1)
     */
    private fun usingOptimizedDP(s: String): Int {
        var (memo, result) = 0 to 1

        (s.length - 1 downTo 0).forEach { index ->
            var tmp = if (s[index] == '0') 0 else result

            if (index + 1 < s.length && (s[index] == '1' || (s[index] == '2' && s[index + 1] < '7'))) {
                tmp += memo
            }
            memo = result
            result = tmp
        }

        return result
    }

    @Test
    fun `입력받은 문자열의 디코딩 가능한 경우의 수를 반환한다`() {
        numDecodings("12") shouldBe 2
        numDecodings("226") shouldBe 3
        numDecodings("06") shouldBe 0
        numDecodings("1011") shouldBe 2
        numDecodings("10112266") shouldBe 8
        numDecodings("1025") shouldBe 2
    }
}
