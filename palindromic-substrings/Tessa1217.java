/**
 * palindrome 부분 수열의 개수를 찾으세요.
 */
class Solution {

    /** 시간복잡도: O(n^2), O(1) */
    public int countSubstrings(String s) {

        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            count += checkPalindrome(s, i, i); // 홀수
            count += checkPalindrome(s, i, i + 1); // 짝수
        }

        return count;
    }

    private int checkPalindrome(String s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            count++;
            left--;
            right++;
        }
        return count;
    }
}

