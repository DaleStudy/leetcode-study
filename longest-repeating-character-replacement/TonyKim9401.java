// TC: O(26 * n) => O(n)
// iterates 26 times at the first for-loop, while loop O(n)
// SC: O(1)
class Solution {
    public int characterReplacement(String s, int k) {
        int ans = 0;
        int n = s.length();
        for (char c = 'A'; c <= 'Z'; c++) {
            int i = 0, j = 0, replaced = 0;
            while (j < n) {
                if (s.charAt(j) == c) {
                    j += 1;
                } else if (replaced < k) {
                    j += 1;
                    replaced++;
                } else if (s.charAt(i) == c) {
                    i += 1;
                } else {
                    i += 1;
                    replaced -= 1;
                }
                ans = Math.max(ans, j - i);
            }
        }
        return ans;
    }
}
