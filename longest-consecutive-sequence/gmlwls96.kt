package leetcode_study

class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        nums.sort()
        val consecutiveArray = IntArray(nums.size)
        var maxCount = 0
        for (i in nums.lastIndex - 1 downTo (0)) {
            if (nums[i] + 1 == nums[i + 1]) {
                consecutiveArray[i] += consecutiveArray[i + 1] + 1
                if (consecutiveArray[i] > maxCount) {
                    maxCount = consecutiveArray[i]
                }
            }
        }
        return maxCount + 1
    }
}
