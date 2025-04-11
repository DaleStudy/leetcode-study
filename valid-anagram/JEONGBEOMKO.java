import java.util.HashMap;
import java.util.Map;

public class Solution {
    /*
    time complexity: O(n)
    space complexity: O(1)
     */
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> sFrequency = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            sFrequency.put(s.charAt(i), sFrequency.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            if (sFrequency.getOrDefault(t.charAt(i), 0) != 0) {
                sFrequency.put(t.charAt(i), sFrequency.get(t.charAt(i)) - 1);
            }
        }

        for (int count : sFrequency.values()) {
            if (count != 0) return false;
        }

        return true;
    }
}
