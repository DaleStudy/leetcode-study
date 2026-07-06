class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        val sCharToCount = mutableMapOf<Char, Int>()
        val tCharToCount = mutableMapOf<Char, Int>()

        s.forEach { sCharToCount[it] = (sCharToCount[it] ?: 0) + 1 }
        t.forEach { tCharToCount[it] = (tCharToCount[it] ?: 0) + 1 }

        val sKeys: MutableSet<Char> = sCharToCount.keys
        val tKeys: MutableSet<Char> = tCharToCount.keys

        if (sKeys != tKeys) return false
        sKeys.forEach {
            if (sCharToCount[it] != tCharToCount[it]) {
                return false
            }
        }
        return true
    }
}
