package leetcode_study

class SolutionContainsDuplicate {
    fun containsDuplicate(nums: IntArray): Boolean {
        val size = nums.size
        val numsToSet = nums.toSet()

        return size != numsToSet.size
    }
}
