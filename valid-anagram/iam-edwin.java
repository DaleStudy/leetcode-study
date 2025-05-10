import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            Integer count = sMap.getOrDefault(c, 0);
            sMap.put(c, count + 1);
        }

        Map<Character, Integer> tMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            Integer count = tMap.getOrDefault(c, 0);
            tMap.put(c, count + 1);
        }

        for (char key : sMap.keySet()) {
            if (!sMap.get(key).equals(tMap.get(key))) {
                return false;
            }
            tMap.remove(key);
        }

        return tMap.isEmpty();
    }
}
