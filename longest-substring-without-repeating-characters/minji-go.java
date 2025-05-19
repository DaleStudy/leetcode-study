/**
 * <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">week07-2.longest-substring-without-repeating-characters</a>
 * <li>Description: find the length of the longest substring without duplicate characters</li>
 * <li>Topics: Hash Table, String, Sliding Window   </li>
 * <li>Time Complexity: O(N), Runtime 5ms           </li>
 * <li>Space Complexity: O(L), Memory 44.66MB       </li>
 */

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        int left = 0;

        Map<Character, Integer> chars = new HashMap<>();
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);

            if (chars.containsKey(c) && chars.get(c) >= left) {
                left = chars.get(c) + 1;
            }

            chars.put(c, right);
            max = Math.max(max, right - left + 1);
        }

        return max;
    }
}
