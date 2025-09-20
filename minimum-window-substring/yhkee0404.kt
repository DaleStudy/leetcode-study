class Solution {
    fun minWindow(s: String, t: String): String { // T(m, n) = S(m, n) = O(m + n)
        val counterT = (
            t
            .groupingBy {it} // O(n)
            .eachCount()
        )
        var l = -1
        var r = -1
        val counterS = mutableMapOf<Char, Int>()
        var i = -1
        (
            s
            .withIndex()
            .forEach { // O(m)
                counterS.compute(it.value) {k, v -> if (v == null) 1 else v + 1}
                while (i != it.index && counterS[s[i + 1]]!! > counterT.getOrDefault(s[i + 1], 0)) { // O(m)
                    counterS.compute(s[++i]) {k, v -> v!! - 1}
                }
                if (
                    counterT
                    .all {(k, v) -> counterS.getOrDefault(k, 0) >= v} // O(n)
                ) {
                    if (r == -1 || r - l > it.index - i) {
                        l = i
                        r = it.index
                    }
                }
            }
        )
        return s.substring(l + 1, r + 1) // O(m)
    }
}
