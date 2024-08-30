package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `product-of-array-except-self` {

    fun productExceptSelf(nums: IntArray): IntArray {
        return usingPrefixSum(nums)
    }

    /**
     * 각 인덱스의 전,후를 누적곱을 합하여 이전 연산 결과를 재활용한다.
     * 시간복잡도: O(n), 공간복잡도: O(n)
     */
    private fun usingPrefixSum(nums: IntArray): IntArray {
        val toRight = Array(nums.size) { 1 }
        val toLeft = Array(nums.size) { 1 }

        (0 until nums.size - 1).forEach {
            toRight[it + 1] = toRight[it] * nums[it]
        }
        (nums.size - 1 downTo 1).forEach {
            toLeft[it - 1] = toLeft[it] * nums[it]
        }

        return nums.indices
            .map { toRight[it] * toLeft[it] }
            .toIntArray()
    }

    @Test
    fun `입력받은 배열을 순회하며 자기 자신을 제외한 나머지 원소들의 곱한 값을 배열로 반환한다`() {
        productExceptSelf(intArrayOf(2,3,4,5)) shouldBe intArrayOf(60,40,30,24)
        productExceptSelf(intArrayOf(1,2,3,4)) shouldBe intArrayOf(24,12,8,6)
        productExceptSelf(intArrayOf(-1,1,0,-3,3)) shouldBe intArrayOf(0,0,9,0,0)
    }
}
