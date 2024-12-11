class Solution {
    fun isPalindrome(s: String): Boolean {
        val filterStr = s
            .lowercase()
            .filter { it in 'a'..'z' }
        if (filterStr.isEmpty()) return true
        for (i in 0..filterStr.lastIndex / 2) {
            if (filterStr[i] != filterStr[filterStr.lastIndex - i]) return false
        }
        return true
    }
}
