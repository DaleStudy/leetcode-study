package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max
import kotlin.math.min

class `maximum-product-subarray` {

    /**
     * 현재의 값, 이전 위치의 최대 누적곱, 이전 위치의 최소 누적곱 이 세 개를 비교하여 한 번의 순회로 최대 값을 반환한다.
     * 음수와 음수가 곱해져 최대 값이 도출될 수 있기에 DP 배열을 두 개 생성한다.
     * TC: O(n), SC: O(n)
     */
    fun maxProduct(nums: IntArray): Int {
        val (min, max) = IntArray(nums.size) { 11 }.apply { this[0] = nums[0] } to IntArray(nums.size) { -11 }.apply { this[0] = nums[0] }
        var result = max(-11, nums[0])
        for (index in 1 until nums.size) {
            max[index] = max(max(nums[index], nums[index] * max[index - 1]), nums[index] * min[index - 1])
            min[index] = min(min(nums[index], nums[index] * max[index - 1]), nums[index] * min[index - 1])
            result = max(max(min[index], max[index]), result)
        }

        return result
    }

    @Test
    fun `입력받은 정수 배열의 가장 큰 곱을 반환한다`() {
        maxProduct(intArrayOf(2,3,-2,4)) shouldBe 6
        maxProduct(intArrayOf(-2,0,-1)) shouldBe 0
        maxProduct(intArrayOf(-10)) shouldBe -10
        maxProduct(intArrayOf(-2,3,-4)) shouldBe 24
    }
}
