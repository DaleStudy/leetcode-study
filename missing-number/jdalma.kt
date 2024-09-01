package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `missing-number` {

    fun missingNumber(nums: IntArray): Int {
        return usingSum(nums)
    }

    /**
     * 1. 배열을 추가로 생성하여 존재하는 정수의 인덱스에 true를 저장하여, false인 인덱스를 반환한다.
     * TC: O(n), SC: O(n)
     */
    private fun usingIndex(nums: IntArray): Int {
        val existed = BooleanArray(nums.size + 1)
        nums.forEach { existed[it] = true }

        existed.forEachIndexed { i, e ->
            if (!e) return i
        }
        return -1
    }

    /**
     * 2. 0부터 정수 배열의 사이즈만큼 정수를 합산하여 기대하는 합산과 뺀 결과를 반환한다.
     * TC: O(n), SC: O(1)
     */
    private fun usingSum(nums: IntArray): Int {
        val size = nums.size
        return nums.fold((size + 1) * size / 2) { acc , i -> acc - i }
    }

    @Test
    fun `입력받은 정수 배열에서 비어있는 정수를 반환한다`() {
        missingNumber(intArrayOf(3,2,1)) shouldBe 0
        missingNumber(intArrayOf(3,0,1)) shouldBe 2
        missingNumber(intArrayOf(9,6,4,2,3,5,7,0,1)) shouldBe 8
    }
}
