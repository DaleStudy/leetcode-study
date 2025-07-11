/**
 * <a href="https://leetcode.com/problems/longest-repeating-character-replacement/">week8-2.longest-repeating-character-replacement</a>
 * <li>Description: Return the length of the longest substring containing the same letter you can get after changing the character to any other uppercase English character</li>
 * <li>Topics: Hash Table, String, Sliding Window</li>
 * <li>Time Complexity: O(K), Runtime 7ms       </li>
 * <li>Space Complexity: O(1), Memory 44.85MB   </li>
 */

class Solution {
    public int characterReplacement(String s, int k) {
        int left = 0;
        int maxCount = 0;
        int[] count = new int[26];
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            count[c - 'A']++;
            maxCount = Math.max(maxCount, count[c - 'A']);

            while (right - left + 1 > maxCount + k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
