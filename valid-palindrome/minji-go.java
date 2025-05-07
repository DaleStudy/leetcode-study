/**
 * <a href="https://leetcode.com/problems/valid-palindrome/">week03-1.valid-palindrome</a>
 * <li>Description: return true if it is a palindrome </li>
 * <li>Topics: Two Pointers, String             </li>
 * <li>Time Complexity: O(N), Runtime 13ms      </li>
 * <li>Space Complexity: O(N), Memory 45.55MB   </li>
 */
class Solution {
    public boolean isPalindrome(String s) {
        String str = s.toLowerCase().replaceAll("[^0-9a-z]", "");

        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
