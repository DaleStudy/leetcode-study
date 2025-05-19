class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        return nums.size != nums.distinct().size
    }
}
