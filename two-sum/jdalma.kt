package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `two-sum` {

    fun twoSum(nums: IntArray, target: Int): IntArray {
        return usingMapOptimized(nums, target)
    }

    /**
     * 1. map을 활용
     * TC: O(n), SC: O(n)
     */
    private fun usingMap(nums: IntArray, target: Int): IntArray {
        val map = nums.withIndex().associate { it.value to it.index }

        nums.forEachIndexed { i, e ->
            val diff: Int = target - e
            if (map.containsKey(diff) && map[diff] != i) {
                return intArrayOf(i , map[diff]!!)
            }
        }
        return intArrayOf()
    }

    /**
     * 2. map에 모든 값을 초기화할 필요가 없기에, nums를 순회하며 확인한다.
     * TC: O(n), SC: O(n)
     */
    private fun usingMapOptimized(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()

        for (index in nums.indices) {
            val diff = target - nums[index]
            if (map.containsKey(diff)) {
                return intArrayOf(map[diff]!!, index)
            }
            map[nums[index]] = index
        }

        return intArrayOf()
    }

    @Test
    fun `정수 배열과 목푯값을 입력받아 목푯값을 만들 수 있는 정수 배열의 원소들 중 두 개의 원소의 인덱스를 반환한다`() {
        twoSum(intArrayOf(2,7,11,15), 9) shouldBe intArrayOf(0,1)
        twoSum(intArrayOf(3,2,4), 6) shouldBe intArrayOf(1,2)
        twoSum(intArrayOf(3,3), 6) shouldBe intArrayOf(0,1)
    }
}
