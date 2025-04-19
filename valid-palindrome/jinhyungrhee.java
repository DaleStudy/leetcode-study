class Solution {
    public boolean isPalindrome(String s) {

        int len = s.length();

        String target = "";
        for (int i = 0; i < len; i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                target += Character.toLowerCase(s.charAt(i));
            }
        }

        String reversedTarget = "";
        for (int i = len - 1; i >= 0; i--) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                reversedTarget += Character.toLowerCase(s.charAt(i));
            }
        }

        if (target.length() == 0) return true;
        for (int i = 0; i < target.length(); i++) {
            if (target.charAt(i) != reversedTarget.charAt(i)) return false;
        }
        return true;
    }
}
