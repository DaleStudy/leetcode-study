/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * time: O(N)
 * space: O(N)
 */
class Solution {

    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int k = 0;
        int longest = 0;
        int mapVersion = 0;
        Map<Character, Integer> charMap = new HashMap<>();
        while (start + k < s.length()) {
            char cur = s.charAt(start + k);
            int curVersion = charMap.getOrDefault(cur, 0);
            if (curVersion > mapVersion) {
                longest = Math.max(longest, k);
                start++;
                k = 0;
                mapVersion = curVersion;
            } else {
                charMap.put(cur, mapVersion + 1);
                k++;
            }
        }
        longest = Math.max(longest, k);
        return longest;
    }
}
