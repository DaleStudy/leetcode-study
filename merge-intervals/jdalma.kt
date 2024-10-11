package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `merge-intervals` {

    data class CustomRange(
        var start: Int,
        var end: Int
    ) {
        fun isMergePossible(s: Int) = s <= this.end
    }

    /**
     * TC: O(n log n), SC: O(n)
     */
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        val sorted = intervals.sortedWith { i1, i2 -> i1[0].compareTo(i2[0]) }
        val result = mutableListOf<CustomRange>()

        var tmp = sorted.first().let {
            CustomRange(it[0], it[1])
        }
        result.add(tmp)
        for (interval in sorted) {
            if (tmp.isMergePossible(interval[0])) {
                tmp.end = max(interval[1], tmp.end)
            } else {
                tmp = CustomRange(interval[0], interval[1])
                result.add(tmp)
            }
        }

        return result.map { intArrayOf(it.start, it.end) }
            .toTypedArray()
    }

    @Test
    fun `2차원 배열의 원소인 start와 end만큼 병합한 결과를 반환한다`() {
        merge(
            arrayOf(
                intArrayOf(2,6),
                intArrayOf(8,10),
                intArrayOf(15,18),
                intArrayOf(1,3)
            )
        ) shouldBe arrayOf(
            intArrayOf(1,6),
            intArrayOf(8,10),
            intArrayOf(15,18)
        )

        merge(
            arrayOf(
                intArrayOf(1,4),
                intArrayOf(0,4)
            )
        ) shouldBe arrayOf(
            intArrayOf(0,4)
        )

        merge(
            arrayOf(
                intArrayOf(1,4),
                intArrayOf(0,1)
            )
        ) shouldBe arrayOf(
            intArrayOf(0,4)
        )
    }
}
