import java.util.Stack;

public class Sol35229 {

    class Solution {
        public boolean isPalindrome(String s) {
            s = s.toLowerCase().replaceAll("[^a-z0-9]", "");
            int left = 0;
            int right = s.length() - 1;
            while (left < right) {
                if (s.charAt(left) != s.charAt(right)) {
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }
//        boolean isLowerCase(Character c) {
//            return (int) c > 96 && (int) c < 123 ? true : false;
//        }
    }
}

