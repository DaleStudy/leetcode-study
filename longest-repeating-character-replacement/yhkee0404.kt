class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        val cnts = MutableList<Int>('Z'.code - 'A'.code + 1) {0}
        var max_cnt = 0
        var ans = 0
        var i = 0
        var j = 0
        while (j != s.length) { // T(n) = S(n) = O(n)
            while (j != s.length) {
                val diff = j - i - max_cnt
                if (diff > k) {
                    break
                }
                val d = s[j].code - 'A'.code
                if (diff == k && max_cnt != cnts[d]) {
                    break
                }
                j++
                max_cnt = maxOf(max_cnt, ++cnts[d])
            }
            ans = maxOf(ans, j - i)
            val d = s[i++].code - 'A'.code
            cnts[d]--
        }
        return ans
    }
}
