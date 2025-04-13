class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val countMap = nums.groupBy { it }
            .mapValues { it.value.size }
        val sortedList = countMap.entries
            .sortedByDescending { it.value }
            .map { it.key }
        return sortedList.subList(0, k).toIntArray()
    }
}
