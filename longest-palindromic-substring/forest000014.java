/*
# Time Complexity: O(n^2)
# Spcae Complexity: O(1)
*/
class Solution {
    public String longestPalindrome(String s) {
        String ans = "";
        for (int i = 0; i < s.length(); i++) {
            int l = i;
            int r = i;

            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > ans.length()) ans = s.substring(l, r + 1);
                l--;
                r++;
            }

            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > ans.length()) ans = s.substring(l, r + 1);
                l--;
                r++;
            }
        }

        return ans;
    }
}
