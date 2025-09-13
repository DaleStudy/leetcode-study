class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        val cnts = MutableList<Int>('Z'.code - 'A'.code + 1) {0}
        val queue = PriorityQueue<List<Int>>() {a, b -> b.first() - a.first()}
        queue.offer(listOf(0, -1))
        var ans = 0
        var i = 0
        var j = 0
        while (j != s.length) { // T(n) = S(n) = O(nlogn)
            while (queue.size > 1) {
                val u = queue.peek()
                if (u.first() == cnts[u.last()]) {
                    break
                }
                queue.poll()
            }
            while (j != s.length) {
                val diff = j - i - queue.peek().first()
                if (diff > k) {
                    break
                }
                val d = s[j].code - 'A'.code
                if (diff == k && queue.peek().first() != cnts[d]) {
                    break
                }
                j++
                queue.offer(listOf(++cnts[d], d)) // O(logn)
            }
            ans = maxOf(ans, j - i)
            val d = s[i++].code - 'A'.code
            queue.offer(listOf(--cnts[d], d)) // O(logn)
        }
        return ans
    }
}
