package leetcode_study
class SolutionTopKFrequentElements {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val numsCount = mutableMapOf<Int, Int>()
        for (num in nums) {
            val value = numsCount.getOrDefault(num, 0)
            numsCount[num] = value + 1
        }
        val sortedNumsCount = numsCount.entries
            .sortedByDescending { it.value }
            .associate { it.toPair() }

        return sortedNumsCount.keys.take(k).toIntArray()
    }
}
