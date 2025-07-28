class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val frequency = nums.toList().groupingBy { it }.eachCount()

        return frequency
            .toList()
            .sortedByDescending { it.second }
            .take(k)
            .map { it.first }
            .toIntArray()
    }
}
