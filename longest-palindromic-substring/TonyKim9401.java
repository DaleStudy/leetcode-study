// TC: O(n^2)
// for loop & nested while loop => total O(n^2)
// SC: O(1)
// uses only constant space => O(1)
class Solution {
    public String longestPalindrome(String s) {
        int right = 0;
        int left = 0;

        for (int i = 0; i < s.length(); i++) {
            int even = pad(s, i, i);
            int odd = pad(s, i, i+1);
            int max = Math.max(even, odd);

            if (max > (right - left)) {
                right = i + (max + 1) / 2;
                left = i - max / 2;
            }
        }

        return s.substring(left, right+1);
    }

    private int pad(String s, int start, int end) {
        while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            start -= 1;
            end += 1;
        }
        return start - end;
    }
}
