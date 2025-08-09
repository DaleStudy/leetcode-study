import java.util.Locale.getDefault

class Solution {
    fun isPalindrome(s: String): Boolean {
        if (s.isBlank()) return true
        val cleanedString = s.trim().filter { it.isLetterOrDigit() }.lowercase(getDefault())
        return cleanedString == cleanedString.reversed()
    }
}
