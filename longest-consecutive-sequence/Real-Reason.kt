package leetcode_study
class SolutionLongestConsecutiveSequence {
    fun longestConsecutive(nums: IntArray): Int {
        nums.sort()
        var cnt = 0
        var maxCnt = 0
        nums.forEachIndexed { i, _ ->
            if (i == 0) {
                cnt = 1
            }
            else if (nums[i-1] == nums[i] - 1) {
                cnt++
            }
            else if (nums[i - 1] == nums[i]) {
                return@forEachIndexed
            } else {
                cnt = 1
            }
            maxCnt = maxOf(maxCnt, cnt)
        }

        return maxCnt
    }
}
