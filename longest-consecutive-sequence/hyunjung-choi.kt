package leetcode_study

class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        if (nums.isEmpty()) return 0

        val sortedNums = nums.sorted()
        var maxLength = 1
        var currentLength = 1

        for (i in 1 until sortedNums.size) {
            when {
                sortedNums[i] == sortedNums[i - 1] -> continue
                sortedNums[i] == sortedNums[i - 1] + 1 -> {
                    currentLength++
                    maxLength = maxOf(maxLength, currentLength)
                }
                else -> currentLength = 1
            }
        }

        return maxLength
    }
}
