import java.util.HashMap;
import java.util.Map;

public class Solution {

    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> charMap = new HashMap<>();

        char[] sArr = s.toCharArray();
        for (char sa : sArr) {
            charMap.put(sa, charMap.getOrDefault(sa, 0) + 1);
        }

        char[] tArr = t.toCharArray();
        for (char ta : tArr) {
            charMap.put(ta, charMap.getOrDefault(ta, 0) - 1);
        }

        for (int cnt : charMap.values()) {
            if (cnt != 0) {
                return false;
            }
        }

        return true;

    }
}
