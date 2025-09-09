// Time Complexity: O(n*n), n: s.length()
// Space Complexity: O(1)
class Solution {
    public int countSubstrings(String s) {
        int cnt = 0;

        for (int i = 0; i < s.length(); i++, cnt++) {   // i: center of palindrom
            // odd number palindrom: e.g. aba
            int left = i-1, right = i+1;

            while (left >= 0 && right < s.length()) {
                if (s.charAt(left) != s.charAt(right)) {
                    break;
                }
                cnt++;
                left--;
                right++;
            }

            // even number palindrom: e.g. abba
            left = i;
            right = i+1;

            while (left >= 0 && right < s.length()) {
                if (s.charAt(left) != s.charAt(right)) {
                    break;
                }
                cnt++;
                left--;
                right++;
            }
        }

        return cnt;
    }
}
