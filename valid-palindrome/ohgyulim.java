class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();

        for (char ch : s.toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                sb.append(Character.toLowerCase(ch));
            }
        }

        for (int i = 0; i < sb.length(); i++) {
            int left = i;
            int right = sb.length() - i - 1;

            if (left >= right) return true;
            if (sb.charAt(left) != sb.charAt(right)) return false;
        }

        return true;
    }
}