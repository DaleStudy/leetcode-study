package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `longest-increasing-subsequence` {

    fun lengthOfLIS(nums: IntArray): Int {
        return usingBinarySearch(nums)
    }

    /**
     * 이전 최장 수열 길이를 재사용한다.
     * TC: O(n^2), SC: O(n)
     */
    private fun usingDP(nums: IntArray): Int {
        val dp = IntArray(nums.size) { 1 }

        for (i in 1 until nums.size) {
            for (j in 0 until i) {
                if (nums[i] > nums[j] && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1
                }
            }
        }

        return dp.max()
    }

    /**
     * 최장 수열을 직접 갱신한다.
     * TC: O(n * log n), SC: O(n)
     */
    private fun usingBinarySearch(nums: IntArray): Int {

        fun binarySearch(list: List<Int>, number: Int): Int {
            var (low, high) = 0 to list.size - 1

            while (low <= high) {
                val mid = (low + high) / 2
                if (list[mid] == number) {
                    return mid
                } else if (list[mid] < number) {
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }
            return low
        }

        val result = mutableListOf<Int>()

        for (num in nums) {
            if (result.isEmpty() || result.last() < num) {
                result.add(num)
            } else {
                result[binarySearch(result, num)] = num
            }
        }

        return result.size
    }

    @Test
    fun name() {
        // lengthOfLIS(intArrayOf(10,9,2,5,3,7,101,18)) shouldBe 4
        // lengthOfLIS(intArrayOf(0,1,0,3,2,3)) shouldBe 4
        // lengthOfLIS(intArrayOf(0,1,2,3,4,5,6,7)) shouldBe 8
        lengthOfLIS(intArrayOf(4,10,4,3,8,9)) shouldBe 3
    }
}
