import kotlin.math.max

class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        val numsSet = nums.toHashSet()
        var maxLength = 0
        for (num in numsSet) {
            if (num - 1 in numsSet) {
                continue
            }
            var length = 1
            while (num + length in numsSet) {
                ++length
            }
            maxLength = max(length, maxLength)
        }
        return maxLength
    }
}
