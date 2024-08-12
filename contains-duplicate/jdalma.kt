package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test

class `contains-duplicate`{

    fun containsDuplicate(nums: IntArray): Boolean {
        return third(nums)
    }

    // 시간초과
    // 시간복잡도: O(n^2), 공간복잡도: O(1)
    private fun first(nums: IntArray): Boolean {
        nums.forEachIndexed { i, e1 ->
            nums.forEachIndexed { j, e2 ->
                if (i != j && e1 == e2) {
                    return true
                }
            }
        }
        return false
    }

    // 시간복잡도:  O(n * log(n)), 공간복잡도: O(1)
    private fun second(nums: IntArray): Boolean {
        nums.sort() // DualPivotQuicksort -> O(n log(n))
        for (index in 1 until nums.size) {
            val prev = nums[index - 1]
            val curr = nums[index]
            if (prev == curr) {
                return true
            }
        }
        return false
    }

    // 시간복잡도: O(n), 공간복잡도: O(n)
    private fun third(nums: IntArray): Boolean {
        val set = nums.toSet()
        return nums.size != set.size
    }

    @Test
    fun 동일한_원소가_존재하면_true를_반환한다() {
        val nums1 = intArrayOf(1, 2, 3, 1)
        val nums2 = intArrayOf(1, 2, 3, 2)
        val nums3 = intArrayOf(1, 1, 1, 1, 3, 3, 4, 3, 2, 4, 2)

        containsDuplicate(nums1) shouldBeEqual true
        containsDuplicate(nums2) shouldBeEqual true
        containsDuplicate(nums3) shouldBeEqual true
    }

    @Test
    fun 동일한_원소가_존재하지_않으면_false를_반환한다() {
        val nums1 = intArrayOf(1, 2, 3, 4)
        val nums2 = intArrayOf(1, 5, 7)

        containsDuplicate(nums1) shouldBeEqual false
        containsDuplicate(nums2) shouldBeEqual false
    }
}
