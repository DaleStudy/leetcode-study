// Time Complexity: O(n), n: s.length()
// Space Complexity: O(n), n: s.length()
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int begin = 0;
        int end = 0;
        int maxLength = 0;

        Set<Character> letterSet = new HashSet<>();
        while (end < s.length()) {
            // if the letter is not in the hashset, then add it into hashset and move end pointer
            if (!letterSet.contains(s.charAt(end))) {
                letterSet.add(s.charAt(end));
                ++end;
                maxLength = Math.max(maxLength, end - begin); // update maxlength
            } else { // if the letter is in the hashset, then remove it and move begin pointer
                letterSet.remove(s.charAt(begin));
                ++begin;
            }
        }

        return maxLength;
    }
}