/**
 * https://leetcode.com/problems/valid-anagram/
 * TC : O(N)
 * SC : O(1)
 */
class Solution_242 {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] alpCnt = new int[26];

        for (int i=0; i<s.length(); i++) {
            alpCnt[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < s.length(); i++) {
            if (alpCnt[t.charAt(i) - 'a'] < 1) {
                return false;
            }
            alpCnt[t.charAt(i) - 'a']--;
        }
        return true;
    }
}
