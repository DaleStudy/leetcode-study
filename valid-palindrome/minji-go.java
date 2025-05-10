/**
 * <a href="https://leetcode.com/problems/valid-palindrome/">week03-1.valid-palindrome</a>
 * <li>Description: return true if it is a palindrome </li>
 * <li>Topics: Two Pointers, String             </li>
 * <li>Time Complexity: O(N), Runtime 2ms       </li>
 * <li>Space Complexity: O(1), Memory 42.75MB   </li>
 */
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            char charLeft = s.charAt(left);
            char charRight = s.charAt(right);
            if (isNotValidCharacter(charLeft)) {
                left++;
                continue;
            }
            if (isNotValidCharacter(charRight)) {
                right--;
                continue;
            }

            if (Character.toLowerCase(charLeft) != Character.toLowerCase(charRight)) {
                return false;
            }
            left++;
            right--;
        }
        return true;

    }

    private boolean isNotValidCharacter(char c) {
        if ((c >= '0' && c <= '9')
                || (c >= 'a' && c <= 'z')
                || (c >= 'A' && c <= 'Z')) {
            return false;
        }
        return true;
    }
}
