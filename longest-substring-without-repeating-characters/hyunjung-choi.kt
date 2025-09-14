/**
 * 시간복잡도: O(n)
 * 공간복잡도: O(min(m,n)) - m은 문자셋 크기
 */

class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val seen = mutableSetOf<Char>()
        var left = 0
        var maxLength = 0

        for (right in s.indices) {
            while (s[right] in seen) {
                seen.remove(s[left])
                left++
            }

            seen.add(s[right])
            maxLength = maxOf(maxLength, right - left + 1)
        }

        return maxLength
    }
}
