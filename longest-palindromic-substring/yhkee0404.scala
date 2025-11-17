import scala.collection.mutable.ArrayBuffer

object Solution {
    def longestPalindrome(s: String): String = {
        val list = ArrayBuffer[Char]()
        for (c <- s) {
            list += c
            list += '\u0000'
        }
        val dp = Array.fill(list.size - 1)(0)
        var lastR = -1
        var lastMid = -1
        var maxD = 0
        var ansL = 0
        var ansR = 0
        var i = 1
        for (i <- 0 until dp.size) { // Manacher T(n) = S(n) = O(n)
            val diff = lastR - i
            var d = if (diff <= 0) 0 else diff min dp((lastMid << 1) - i)
            var l = i - d
            var r = i + d
            while (l != 0 && r != list.size - 1 && list(l - 1) == list(r + 1)) {
                d += 1
                l -= 1
                r += 1
            }
            if (maxD < d) {
                maxD = d
                ansL = l
                ansR = r
            }
            dp(i) = d
            if (lastR < r) {
                lastR = r
                lastMid = i
            }
        }
        val sb = StringBuilder()
        for (i <- ansL to ansR if list(i) != '\u0000') {
            sb.append(list(i))
        }
        sb.toString
    }
}
