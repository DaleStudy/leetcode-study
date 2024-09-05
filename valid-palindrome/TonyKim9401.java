// TC: O(n)
// SC: O(1)
class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            while (!Character.isLetterOrDigit(s.charAt(start)) && start < end) start += 1;
            while (!Character.isLetterOrDigit(s.charAt(end)) && start < end) end -= 1;

            if (Character.toLowerCase(s.charAt(start))
                    != Character.toLowerCase( s.charAt(end))) return false;

            start += 1;
            end -= 1;
        }

        return true;
    }
}
