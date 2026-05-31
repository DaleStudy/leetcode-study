class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val occurrences = HashSet<Int>(nums.size)
        return nums.any { !occurrences.add(it) }
    }
}
