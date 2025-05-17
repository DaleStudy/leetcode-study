/**
 * <a href="https://leetcode.com/problems/decode-ways/">week03-5.decode-ways</a>
 * <li>Description: return the number of ways to decode it </li>
 * <li>Topics: String, Dynamic Programming  </li>
 * <li>Time Complexity: O(N), Runtime 1ms   </li>
 * <li>Space Complexity: O(1), Memory 41.8MB</li>
 */
class Solution {
    public int numDecodings(String s) {
        if (s.charAt(0) == '0') {
            return 0;
        }

        int last2 = 1;
        int last1 = 1;

        for (int i = 1; i < s.length(); i++) {
            int curr = 0;
            if (s.charAt(i) != '0') {
                curr += last1;
            }

            int num = Integer.parseInt(s.substring(i - 1, i + 1));
            if (num >= 10 && num <= 26) {
                curr += last2;
            }

            last2 = last1;
            last1 = curr;
        }

        return last1;
    }
}
