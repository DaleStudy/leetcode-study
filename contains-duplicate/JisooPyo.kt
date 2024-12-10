package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

/**
 * Leetcode
 * 217. Contains Duplicate
 * Easy
 */
class ContainsDuplicate {
    /**
     * Runtime: 17 ms(Beats: 80.99 %)
     * Time Complexity: O(n)
     *   - 배열 순회
     *
     * Memory: 50.63 MB(Beats: 70.32 %)
     * Space Complexity: O(n)
     *   - HashSet에 최악의 경우 배열 원소 모두 저장
     */
    fun containsDuplicate(nums: IntArray): Boolean {
        val set = hashSetOf<Int>()
        for (i in nums) {
            if (set.contains(i)) {
                return true
            }
            set.add(i)
        }
        return false
    }

    @Test
    fun test() {
        containsDuplicate(intArrayOf(1, 2, 3, 1)) shouldBe true
        containsDuplicate(intArrayOf(1, 2, 3, 4)) shouldBe false
        containsDuplicate(intArrayOf(1, 1, 1, 3, 3, 4, 3, 2, 4, 2)) shouldBe true
    }
}
