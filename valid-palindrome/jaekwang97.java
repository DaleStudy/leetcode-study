import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        String lower = s.toLowerCase();

        int left = 0;
        int right = lower.length() - 1;

        while (left < right) {
            if (!Character.isLetterOrDigit(lower.charAt(left))) {
                left++;
                continue;
            }

            if (!Character.isLetterOrDigit(lower.charAt(right))) {
                right--;
                continue;
            }

            if (lower.charAt(left) != lower.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
