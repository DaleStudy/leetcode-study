/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * time: O(N)
 * space: O(1)
 */
class Solution {

    public int characterReplacement(String s, int k) {
        int[] alp = new int[26];
        int start = 0;
        int maxCnt = 0;
        int maxLen = 0;
        for (int end = 0; end < s.length(); end++) {
            maxCnt = Math.max(maxCnt, ++alp[s.charAt(end) - 'A']);
            while (end - start + 1 - maxCnt > k) {
                alp[s.charAt(start) - 'A']--;
                start++;
            }
            maxLen = Math.max(maxLen, end - start + 1);
        }
        return maxLen;
    }
}
