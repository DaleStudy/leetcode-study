class Solution {
    // 알고리즘 : brute-force
    /** 풀이
     * 1. 모든 substring을 전부 뽑아낸다.
     * 2. 해당 substring이 palindrome인지 체크한다.
     */
    // 시간 : O(n^3)
    fun countSubstrings(s: String): Int {
        var count = 0
        for (len in 1..s.length) { // 길이
            for (i in 0..(s.length - len)) { // i : sub string start index.
                if (checkPalindrome(s.substring(i, i + len))) {
                    count++
                }
            }
        }
        return count
    }

    private fun checkPalindrome(subStr: String): Boolean {
        return if (subStr.length == 1) {
            true
        } else {
            val reverse = subStr.reversed()
            subStr == reverse
        }
    }
}
