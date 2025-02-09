package leetcode_study

class `Real-Reason` {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        for (startIdx in 0..< nums.size - 1) {
            val firstNum = nums[startIdx]
            for (endIdx in startIdx + 1..< nums.size) {
                val secondNum = nums[endIdx]
                if (target == firstNum + secondNum) {
                    return intArrayOf(startIdx, endIdx)
                }
            }
        }
        throw RuntimeException("There is no solution")
    }
}
