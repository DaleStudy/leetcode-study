/**
 * <a href="https://leetcode.com/problems/longest-palindromic-substring/">week15-3. longest-palindromic-substring</a>
 * <li>Description: Given a string s, return the longest palindromic substring in s</li>
 * <li>Topics: Two Pointers, String, Dynamic Programming</li>
 * <li>Time Complexity: O(N), Runtime 15ms   </li>
 * <li>Space Complexity: O(N), Memory 42.13MB</li>
 */

class Solution {
    public String longestPalindrome(String s) {
        int start = 0;
        int maxLength = 1;

        for (int i = 0; i < s.length(); i++) {
            int len1 = findPalindrome(s, i, i);
            int len2 = findPalindrome(s, i, i + 1);

            int len = Math.max(len1, len2);
            if (len > maxLength) {
                maxLength = len;
                start = i - (len - 1) / 2;
            }
        }

        return s.substring(start, start + maxLength);
    }

    public int findPalindrome(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1;
    }
}
