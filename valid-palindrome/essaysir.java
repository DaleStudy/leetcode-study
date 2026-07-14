class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }

        String result = sb.toString();
        char[] x = result.toCharArray();
        for (int i = 0; i < x.length / 2; i++) {
            if (x[i] != x[x.length - i - 1]) {
                return false;
            }
        }
        return true;
    }
}
