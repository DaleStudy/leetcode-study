class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) return false

        val charCount = mutableMapOf<Char, Int>()

        s.forEach { ch ->
            charCount.put(ch, charCount.getOrDefault(ch, 0) + 1)
        }

        t.forEach { ch ->
            val count = charCount.getOrDefault(ch, 0)
            if (count == 0) return false
            charCount[ch] = count - 1
        }

        return true
    }
}
