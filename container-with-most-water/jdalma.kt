package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

typealias Element = Pair<Int,Int>

class `container-with-most-wate` {

    /**
     * 투 포인터를 활용하여 높이가 낮은 인덱스의 값을 한 칸씩 이동하며 최대 높이를 반환한다.
     * TC: O(n), SC: O(1)
     */
    fun maxArea(height: IntArray): Int {
        var (left, right) = 0 to height.size - 1
        var result = 0

        while (left < right) {
            result = max(result, extent(Element(height[left], left), Element(height[right], right)))
            if (height[left] < height[right]) {
                left++
            } else {
                right--
            }
        }
        return result
    }

    private fun extent(e1: Element, e2: Element): Int {
        return min(e1.first, e2.first) * abs(e1.second - e2.second)
    }

    @Test
    fun `입력받은 높이를 표현하는 정수 배열에서 받을 수 있는 최대의 물의 양을 반환한다`() {
        maxArea(intArrayOf(1,8,6,2,5,4,8,3,7)) shouldBe 49
    }
}
