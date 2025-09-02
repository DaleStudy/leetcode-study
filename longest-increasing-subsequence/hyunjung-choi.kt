class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        val tails = mutableListOf<Int>()

        for (num in nums) {
            val pos = binarySearchLeftmost(tails, num)

            if (pos == tails.size) {
                tails.add(num)
            } else {
                tails[pos] = num
            }
        }

        return tails.size
    }

    fun binarySearchLeftmost(list: List<Int>, target: Int): Int {
        var left = 0
        var right = list.size

        while (left < right) {
            val mid = left + (right - left) / 2
            if (list[mid] < target) {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }
}
