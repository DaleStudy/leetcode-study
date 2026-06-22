typealias Number = Int
typealias Index = Int

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val occurrences = HashMap<Number, Index>(nums.size)
        nums.forEachIndexed { index, num ->
            occurrences[target - num]?.let { complementIndex ->
                return intArrayOf(index, complementIndex)
            }
            occurrences[num] = index
        }
        return intArrayOf()
    }
}
