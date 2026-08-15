/**
TC: O(26n) = O(n)
SC: O(26) = O(1)
 */
class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        var left = 0
        val charToCount = mutableMapOf<Char, Int>()
        var maxFrequency = 0

        for (right in s.indices) {
            val added = s[right]
            charToCount[added] = (charToCount[added] ?: 0) + 1

            // 교체 횟수가 k를 넘으면 왼쪽을 당겨 윈도우 축소
            while ((right - left + 1) - charToCount.values.max() > k) {
                val removed = s[left]
                charToCount[removed] = charToCount.getValue(removed) - 1
                left++
            }

            maxFrequency = maxOf(maxFrequency, right - left + 1)
        }

        return maxFrequency
    }
}
