// TC: O(n)
// SC: O(n)
class Solution {
    public boolean isPalindrome(String s) {
        String target = checkString(s);
        return checkPalindrome(target);
    }

    private String checkString(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                sb.append(c);
            }
            if (c >= 'A' && c <= 'Z') {
                c = (char)(c - 'A' + 'a');
                sb.append(c);
            }
            if (c >= '0' && c <= '9') {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    private Boolean checkPalindrome(String target) {
        int start = 0;
        int end = target.length() - 1;

        while (start < end) {
            if (target.charAt(start) != target.charAt(end)) return false;
            start += 1;
            end -= 1;
        }
        return true;
    }
}
