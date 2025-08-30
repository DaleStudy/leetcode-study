/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */

class Solution {
    fun maxArea(height: IntArray): Int {
        var i = 0
        var j = height.size - 1
        var max = 0

        while (i < j) {
            val h = minOf(height[i], height[j])
            max = maxOf(max, (j - i) * h)

            if (height[i] <= height[j]) i++
            else j--
        }

        return max
    }
}
