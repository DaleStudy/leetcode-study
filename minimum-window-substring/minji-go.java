/**
 * <a href="https://leetcode.com/problems/minimum-window-substring/">week9-5. minimum-window-substring</a>
 * <li>Description: return the minimum window substring of s such that every character in t (including duplicates) is included in the window </li>
 * <li>Topics: Hash Table, String, Sliding Window   </li>
 * <li>Time Complexity: O(M+N), Runtime 23ms        </li>
 * <li>Space Complexity: O(1), Memory 45.13MB       </li>
 */
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";

        Map<Character, Integer> tmap = new HashMap<>();
        for (char c : t.toCharArray()) {
            tmap.put(c, tmap.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> smap = new HashMap<>();
        int left = 0, right = 0;
        int tsize = tmap.size();
        int ssize = 0;
        int start = -1, end = s.length();

        while (right < s.length()) {
            char c = s.charAt(right++);
            if (tmap.containsKey(c)) {
                smap.put(c, smap.getOrDefault(c, 0) + 1);
                if (smap.get(c).intValue() == tmap.get(c).intValue()) {
                    ssize++;
                }
            }

            while (ssize == tsize) {
                if (right - left < end - start) {
                    start = left;
                    end = right;
                }

                char l = s.charAt(left++);
                if (tmap.containsKey(l)) {
                    smap.put(l, smap.get(l) - 1);
                    if (smap.get(l).intValue() < tmap.get(l).intValue()) {
                        ssize--;
                    }
                }
            }
        }

        return start == -1 ? "" : s.substring(start, end);
    }
}
