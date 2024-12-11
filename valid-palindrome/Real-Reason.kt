package leetcode_study

class SolutionValidPalindrome {
    fun isPalindrome(s: String): Boolean {
        val sToCharArray = s.toCharArray()
        var startIndex = 0
        var endIndex = sToCharArray.size - 1
        while (startIndex < endIndex) {
            if (!sToCharArray[startIndex].isLetterOrDigit() || sToCharArray[startIndex].isWhitespace()) {
                startIndex++
                continue
            }
            if (!sToCharArray[endIndex].isLetterOrDigit() || sToCharArray[endIndex].isWhitespace()) {
                endIndex--
                continue
            }
            if (sToCharArray[startIndex].lowercase() == sToCharArray[endIndex].lowercase()) {
                startIndex++
                endIndex--
            } else {
                return false
            }
        }

        return true
    }
}
