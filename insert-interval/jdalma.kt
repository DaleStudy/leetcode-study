package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max
import kotlin.math.min

class `insert-interval` {

    /**
     * TC: O(n), SC: O(n)
     */
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        if (intervals.isEmpty()) return arrayOf(newInterval)
        return justIterate(intervals, newInterval)
    }

    private fun justIterate(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        val result = mutableListOf<IntArray>()
        var new: IntArray? = newInterval

        for (interval in intervals) {
            if (new != null) {
                if (new[1] < interval[0]) {
                    // new 범위가 더 앞에 있다
                    result.add(new)
                    result.add(interval)
                    new = null
                } else if (new[0] > interval[1]) {
                    // new 범위가 더 뒤에 있어 다른 범위에 포함될 가능성이 있음
                    result.add(interval)
                } else {
                    new[0] = min(new[0], interval[0])
                    new[1] = max(new[1], interval[1])
                }
            } else {
                result.add(interval)
            }
        }
        if (new != null) {
            result.add(new)
        }
        return result.toTypedArray()
    }

    @Test
    fun name() {
        insert(
            arrayOf(
                intArrayOf(1,2),
                intArrayOf(3,5),
                intArrayOf(6,7),
                intArrayOf(8,10),
                intArrayOf(12,16)
            ),
            intArrayOf(4,8)
        ) shouldBe arrayOf(intArrayOf(1,2), intArrayOf(3,10), intArrayOf(12,16))
    }
}
