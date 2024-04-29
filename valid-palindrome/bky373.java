/**
 * https://leetcode.com/problems/valid-palindrome/
 * TC : O(N)
 * SC : O(1)
 */
class Solution_0125 {

    public boolean isPalindrome(String s) {
        if (s.isBlank() || s.length() == 1) {
            return true;
        }
        s = s.toLowerCase();

        int j = s.length() - 1;
        for (int i = 0; i < j; i++) {
            if (!isAlpNum(s.charAt(i))) {
                continue;
            }
            if (!isAlpNum(s.charAt(j))) {
                i--;
                j--;
                continue;
            }
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            j--;
        }

        return true;
    }

    public boolean isAlpNum(char c) {
        return ('0' <= c && c <= '9') || ('a' <= c && c <= 'z');
    }
}
