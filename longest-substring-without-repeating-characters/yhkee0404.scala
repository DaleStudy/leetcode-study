import scala.util.control.Breaks._

object Solution {
    def lengthOfLongestSubstring(s: String): Int = {
        var ans = 0
        val visited = Array.fill(128)(false) // S(n) = O(1)
        var i = 0
        var j = 0
        while (j != s.length) {
            breakable { // but no continue in scala!
                while (j != s.length) { // T(n) = O(n)
                    if (visited(s(j))) {
                        break
                    }
                    visited(s(j)) = true
                    j += 1
                }
            }
            ans = Math.max(ans, j - i)

            visited(s(i)) = false
            i += 1
        }
        ans
    }
}
